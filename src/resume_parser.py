import re
from .taxonomy import Taxonomy
SECTION_ALIASES={
 'summary':['summary','professional summary','profile','objective'],
 'skills':['skills','technical skills','core skills','technical competencies'],
 'experience':['experience','work experience','professional experience','employment'],
 'projects':['projects','selected projects','academic projects','key projects'],
 'education':['education','academic background'],
 'certifications':['certifications','certificates'],
 'achievements':['achievements','awards','honors'],
 'research':['research','research experience'],
 'publications':['publications','papers'],
}

def _sections(text):
    lines=text.splitlines(); positions=[]
    for i,line in enumerate(lines):
        norm=re.sub(r'[^a-z ]','',line.lower()).strip()
        for key,aliases in SECTION_ALIASES.items():
            if norm in aliases:
                positions.append((i,key)); break
    out={k:'' for k in SECTION_ALIASES}
    for n,(i,key) in enumerate(positions):
        end=positions[n+1][0] if n+1<len(positions) else len(lines); out[key]='\n'.join(lines[i+1:end]).strip()
    return out

def parse_resume(text,tax=None):
    tax=tax or Taxonomy(); sections=_sections(text); lines=[x.strip() for x in text.splitlines() if x.strip()]
    email=re.search(r'[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}',text)
    phone=re.search(r'(?:\+?\d[\d ()-]{7,}\d)',text)
    links=re.findall(r'https?://[^\s)]+',text)
    linkedin=next((x for x in links if 'linkedin.' in x.lower()),''); github=next((x for x in links if 'github.' in x.lower()),''); portfolio=next((x for x in links if x not in {linkedin,github}), '')
    exp_years=_years(text)
    achievements=sections['achievements']
    metrics=re.findall(r'(?<!\w)(?:\d+(?:\.\d+)?\s*%|(?:₹|\$|€)\s*\d[\d,.]*|\d+(?:\.\d+)?\s*(?:x|hours?|days?|records?|users?|million|billion))(?!\w)',text,re.I)
    evidence_words=['presented','communicated','stakeholder','client','leadership','cross-functional','requirements','documented','reported','storytelling','dashboard','presentation']
    comm=[w for w in evidence_words if re.search(r'\b'+re.escape(w)+r'\b',text,re.I)]
    titles=re.findall(r'(?im)^.*\b(?:analyst|scientist|engineer|researcher|developer|intern|consultant|fellow)\b.*$',sections['experience'])
    return {'raw':text,'sections':sections,'contact':{'name':lines[0] if lines else '', 'email':email.group() if email else '', 'phone':phone.group() if phone else '', 'linkedin':linkedin,'github':github,'portfolio':portfolio},'skills':tax.find(text),'experience':sections['experience'],'projects':sections['projects'],'education':sections['education'],'certifications':sections['certifications'],'achievements':achievements,'research':sections['research'],'publications':sections['publications'],'experience_years':exp_years,'metrics':metrics,'communication_evidence':comm,'titles':titles}

def _years(text):
    vals=[int(x) for x in re.findall(r'(\d+)\+?\s*(?:years?|yrs?)',text,re.I)]
    return max(vals) if vals else 0
