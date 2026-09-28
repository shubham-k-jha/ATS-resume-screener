import re

def _bullet_lines(text):
    return [x.strip() for x in text.splitlines() if len(x.strip()) >= 25 and re.match(r'^(?:[-•*▪◦]|\d+[.)])', x.strip())]

def analyze_resume_health(r):
    raw = r.get('raw','')
    sections = r.get('sections', {})
    findings=[]
    strengths=[]
    checks=[]
    def check(label, ok, good, bad, severity='Medium'):
        checks.append({'area':label,'status':'Pass' if ok else 'Needs attention','severity':'' if ok else severity,'finding':good if ok else bad})
        (strengths if ok else findings).append(good if ok else bad)
    check('Contact information', bool(r.get('contact',{}).get('email') and r.get('contact',{}).get('phone')), 'Contact information is detectable.','Email or phone is not clearly detectable.','High')
    check('Professional summary', bool(sections.get('summary','').strip()), 'A summary/profile section is present.','Professional summary is missing or not detected.','High')
    check('Skills section', bool(sections.get('skills','').strip()), 'A dedicated skills section is present.','Dedicated skills section is missing or not detected.','High')
    check('Experience evidence', bool(sections.get('experience','').strip() or sections.get('research','').strip()), 'Experience or research evidence is present.','Experience/research evidence is limited or not detected.','High')
    check('Projects', bool(sections.get('projects','').strip()), 'Projects provide additional evidence.','Projects section is missing or not detected.','Medium')
    check('Education', bool(sections.get('education','').strip()), 'Education is present.','Education section is missing or not detected.','Medium')
    check('LinkedIn', bool(r.get('contact',{}).get('linkedin')), 'LinkedIn URL is detectable.','LinkedIn URL is not detectable.','Low')
    check('GitHub / portfolio', bool(r.get('contact',{}).get('github') or r.get('contact',{}).get('portfolio')), 'A portfolio/repository link is detectable.','No GitHub or portfolio URL is detectable.','Low')
    bullets=_bullet_lines(raw)
    metric_count=len(r.get('metrics',[]))
    check('Achievement evidence', metric_count>=2, f'{metric_count} measurable evidence item(s) detected.','Few measurable outcomes were detected; strengthen bullets where truthful.','Medium')
    long_lines=sum(1 for x in raw.splitlines() if len(x)>180)
    check('Bullet readability', long_lines==0, 'No unusually long text lines detected.','Some lines are unusually long and may be harder to scan or parse.','Low')
    vague=sum(1 for x in bullets if re.search(r'\b(worked on|responsible for|helped with|did|made|handled)\b',x,re.I))
    check('Action-oriented bullets', vague==0, 'Bullets do not show obvious weak lead-ins.','Some bullets use generic phrasing such as "worked on" or "responsible for".','Medium')
    repeated=[]
    verbs=re.findall(r'(?im)^[-•*▪◦]\s*([A-Za-z]+)',raw)
    from collections import Counter
    vc=Counter(v.lower() for v in verbs)
    repeated=[v for v,c in vc.items() if c>=4]
    check('Verb variety', len(repeated)==0, 'No excessive repetition of one bullet-start verb detected.',f'Repeated bullet-start verbs detected: {", ".join(repeated[:4])}.','Low')
    score=100
    for c in checks:
        if c['status']=='Needs attention': score -= {'High':10,'Medium':6,'Low':3}.get(c['severity'],4)
    return {'score':max(0,min(100,score)),'checks':checks,'strengths':strengths,'shortcomings':findings,'metric_count':metric_count}

def role_likeness(r, role_profiles, taxonomy):
    skills=set(r.get('skills',{}))
    out=[]
    for role, profile in role_profiles.items():
        if role=='Custom Role': continue
        priority=set(profile.get('priority',[])); overlap=len(skills & priority)
        base=overlap/max(1,len(priority))*100
        evidence=0
        txt=r.get('raw','').lower()
        if role in ('Data Analyst','BI Analyst','Business Analyst','Product Analyst','Marketing Analyst') and any(x in txt for x in ['dashboard','kpi','report','analysis']): evidence+=10
        if 'Data Scientist' in role and any(x in skills for x in ['Machine Learning','scikit-learn','Statistics']): evidence+=10
        out.append({'role':role,'likeness':round(min(100,base+evidence),1),'matched_priority':sorted(skills & priority)})
    return sorted(out,key=lambda x:x['likeness'],reverse=True)
