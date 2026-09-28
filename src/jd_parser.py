import re
from .taxonomy import Taxonomy
REQ_PATTERNS=r'\b(required|required qualifications|must have|must-have|essential|mandatory|minimum qualifications|basic qualifications|strong experience)\b'
PREF_PATTERNS=r'\b(preferred|nice to have|nice-to-have|bonus|plus|desired|preferred qualifications)\b'

def parse_jd(text,tax=None,selected_role='Custom Role'):
    tax=tax or Taxonomy(); required=set(); preferred=set(); req_evidence=[]; pref_evidence=[]
    # First handle explicit inline labels such as "Required: SQL, Python. Preferred: Power BI".
    chunks=re.split(r'(?i)\bpreferred\s*(?:qualifications?)?\s*:',text,maxsplit=1)
    before_pref=chunks[0]; after_pref=chunks[1] if len(chunks)>1 else ''
    if re.search(r'(?i)\brequired\s*(?:qualifications?)?\s*:',before_pref):
        req_part=re.split(r'(?i)\brequired\s*(?:qualifications?)?\s*:',before_pref,maxsplit=1)[1]
        found=tax.find(req_part); required.update(found); req_evidence.extend(found.keys())
    # Also parse line/state style descriptions.
    state='neutral'
    for line in text.splitlines():
        l=line.lower().strip()
        if re.search(PREF_PATTERNS,l): state='preferred'
        elif re.search(REQ_PATTERNS,l): state='required'
        found=tax.find(line)
        if state=='required': required.update(found); req_evidence.extend(found.keys())
        elif state=='preferred': preferred.update(found); pref_evidence.extend(found.keys())
    if after_pref:
        found=tax.find(after_pref); preferred.update(found); pref_evidence.extend(found.keys())
    all_skills=tax.find(text)
    if not required and not preferred: required=set(all_skills.keys())
    preferred-=required
    role=selected_role if selected_role!='Custom Role' else infer_role(text)
    years=_years(text)
    education=[]
    for term in ['bachelor','master','phd','degree','b.tech','m.tech','mba','msc','m.sc']:
        if re.search(r'\b'+re.escape(term)+r'\b',text,re.I): education.append(term)
    return {'text':text,'role':role,'title':infer_title(text) or role,'required':required,'preferred':preferred,'all':set(all_skills.keys()),'years':years,'education_terms':education,'required_evidence':sorted(set(req_evidence)),'preferred_evidence':sorted(set(pref_evidence))}

def infer_title(text):
    for line in text.splitlines():
        if re.search(r'(?i)\b(data|business|bi|product|marketing|financial|operations|reporting|machine learning|analytics)\s+(analyst|scientist|engineer)\b',line): return line.strip()[:120]
    return ''

def infer_role(text):
    l=text.lower(); mapping=[('Data Scientist',['data scientist','machine learning']),('Product Analyst',['product analyst','product analytics']),('Marketing Analyst',['marketing analyst','marketing analytics']),('BI Analyst',['bi analyst','business intelligence']),('Business Analyst',['business analyst']),('Data Analyst',['data analyst','data analytics']),('Analytics Engineer',['analytics engineer'])]
    for role,terms in mapping:
        if any(t in l for t in terms): return role
    return 'Custom Role'

def _years(text):
    vals=[int(x) for x in re.findall(r'(\d+)\+?\s*(?:years?|yrs?)',text,re.I)]; return max(vals) if vals else 0
