from .config import BASE_WEIGHTS,ROLE_PROFILES
from .semantic_matcher import similarity

def _skill_match(resume,jd,role):
    have=set(resume['skills']); req=set(jd['required']); pref=set(jd['preferred']); allj=req|pref
    priority=set(ROLE_PROFILES.get(role,{}).get('priority',[]))
    rows=[]
    exact_related=0
    for skill in sorted(allj):
        exact=skill in have; related=[]
        if not exact:
            item=resume['skills'].get(skill,{})
            parents=set(item.get('parents',[]))
            for h in have:
                hp=set(resume['skills'][h].get('parents',[]))
                if skill in hp or skill in parents or h in parents: related.append(h)
        match='Exact' if exact else 'Related' if related else 'Missing'
        val=100 if exact else 55 if related else 0
        # Partial evidence is deliberately separated from a true skill absence.
        evidence = _evidence_for_skill(skill,resume)
        if match!='Missing': exact_related+=1
        rows.append({'skill':skill,'importance':'Required' if skill in req else 'Preferred','match_type':match,'score':val,'resume_evidence':evidence,'related_skills':', '.join(related[:4])})
    base=(sum(x['score'] for x in rows)/len(rows)) if rows else 0
    required=(sum(x['score'] for x in rows if x['importance']=='Required')/max(1,len(req)))
    preferred=(sum(x['score'] for x in rows if x['importance']=='Preferred')/max(1,len(pref))) if pref else 100
    role_bonus=(sum(1 for s in priority if s in have)/max(1,len(priority)))*100 if priority else base
    return base,required,preferred,rows,role_bonus

def _evidence_for_skill(skill,resume):
    text=resume['raw']; import re
    for line in text.splitlines():
        if re.search(r'(?<!\w)'+re.escape(skill)+r'(?!\w)',line,re.I): return line.strip()[:220]
    return ''

def evaluate(resume,jd,issues,role=None):
    role=role or jd.get('role','Custom Role'); skill,required,preferred,rows,role_priority=_skill_match(resume,jd,role)
    sem,method=similarity(' '.join([resume['sections'].get('summary',''),resume['experience'],resume['projects']]),jd['text'])
    exp=experience_score(resume,jd); proj=project_score(resume,jd); edu=education_score(resume,jd); ach=achievement_score(resume); comm=communication_score(resume); pres=presentation_score(resume); lang=language_score(resume); ats=100 if not issues else max(0,100-sum({'Critical':25,'High':12,'Medium':6,'Low':2}.get(x['severity'],0) for x in issues))
    tools=tool_score(resume,jd); weights=role_weights(role)
    components={'Skill Match':skill,'Required Skill Coverage':required,'Semantic JD Match':sem*100,'Experience Match':exp,'Project Relevance':proj,'Tools/Technology Match':tools,'Education Match':edu,'Achievement Evidence':ach,'Communication':comm,'Presentation':pres,'English/Language Quality':lang,'ATS Formatting':ats}
    weighted={k:components[k]*weights[key] for k,key in [('Skill Match','skill_match'),('Required Skill Coverage','required_coverage'),('Semantic JD Match','semantic_match'),('Experience Match','experience_match'),('Project Relevance','project_relevance'),('Tools/Technology Match','tools_match'),('Education Match','education_match'),('Achievement Evidence','achievement_evidence'),('Communication','communication'),('Presentation','presentation'),('English/Language Quality','language_quality'),('ATS Formatting','ats_formatting')]}
    overall=sum(weighted.values())/100
    missing_evidence=[x['skill'] for x in rows if x['match_type']=='Missing']
    evidence_gaps=[x['skill'] for x in rows if x['match_type']=='Related']
    return {'overall':round(overall,1),'ats':round(ats,1),'components':{k:round(v,1) for k,v in components.items()},'weights':weights,'rows':rows,'missing_required':[x['skill'] for x in rows if x['importance']=='Required' and x['match_type']=='Missing'],'missing_preferred':[x['skill'] for x in rows if x['importance']=='Preferred' and x['match_type']=='Missing'], 'evidence_gaps':evidence_gaps, 'missing_evidence':missing_evidence,'matched':[x['skill'] for x in rows if x['match_type']=='Exact'],'related':[x['skill'] for x in rows if x['match_type']=='Related'],'semantic_method':method,'role_priority_score':round(role_priority,1),'job_match':round((required*.6+skill*.2+exp*.1+proj*.1),1),'recruiter':round((exp*.3+proj*.25+comm*.15+pres*.1+ats*.2),1)}

def role_weights(role):
    w=dict(BASE_WEIGHTS)
    if 'Data Scientist' in role or 'Machine Learning' in role: w.update(skill_match=20,required_coverage=20,semantic_match=13,experience_match=10,project_relevance=11,tools_match=7,education_match=3,achievement_evidence=5,communication=3,presentation=1,language_quality=2,ats_formatting=5)
    elif 'Analyst' in role: w.update(skill_match=22,required_coverage=20,semantic_match=12,experience_match=10,project_relevance=8,tools_match=8,education_match=3,achievement_evidence=5,communication=5,presentation=2,language_quality=2,ats_formatting=3)
    return w

def experience_score(r,j):
    text=(r['experience']+' '+r['research']).strip(); direct=bool(r['experience']); years=r['experience_years']; req=j.get('years',0)
    if not text:return 0
    score=60 if direct else 45
    if years and req: score += min(30,(years/req)*30)
    elif years: score+=20
    if j['all'] & set(r['skills']): score+=10
    return min(100,score)

def project_score(r,j):
    if not r['projects'].strip():return 0
    overlap=len(set(r['skills'])&j['all']); metrics=min(25,len(r['metrics'])*5); repo=15 if r['contact'].get('github') or 'github' in r['projects'].lower() else 0
    return min(100,35+min(30,overlap*5)+metrics+repo)

def education_score(r,j):
    if not r['education'].strip():return 25
    return 100 if j.get('education_terms') else 85

def achievement_score(r):
    bullets=max(1,len([x for x in r['raw'].splitlines() if x.strip() and len(x.strip())>25])); return min(100,40+min(60,len(r['metrics'])*8)) if bullets else 0

def communication_score(r):
    return min(100,30+len(r['communication_evidence'])*10)

def presentation_score(r):
    hits=sum(1 for x in ['presented','presentation','technical report','seminar','conference','dashboard'] if x in r['raw'].lower()); return min(100,30+hits*15)

def language_score(r):
    text=r['raw']; words=text.split();
    if not words:return 0
    fragments=sum(1 for line in text.splitlines() if len(line)>180); repetition=len(words)-len(set(w.lower() for w in words));
    return max(0,min(100,100-fragments*8-min(25,repetition/max(1,len(words))*100)))

def tool_score(r,j):
    tools={'Git','GitHub','Docker','APIs','AWS','Azure','GCP','Spark','Airflow','dbt','ETL','Data Modeling'}; overlap=len((set(r['skills'])&tools)&j['all']); denom=max(1,len(tools&j['all'])); return min(100,overlap/denom*100) if denom else 75
