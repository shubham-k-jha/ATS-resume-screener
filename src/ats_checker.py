import re

def check(text,meta,contact):
    issues=[]
    def add(severity,message,impact): issues.append({'severity':severity,'message':message,'impact':impact})
    if not contact.get('email'): add('Critical','No email address detected.','Contact information may not be machine-readable.')
    if not contact.get('phone'): add('Medium','No phone number detected.','A recruiter may have limited contact options.')
    if meta.get('scanned_warning'): add('Critical','PDF contains little selectable text and may be scanned/image-based.','Automated parsers may miss most resume content.')
    if meta.get('tables'): add('Medium',f"DOCX contains {meta['tables']} table(s).","Some ATS parsers can read tables inconsistently.")
    if meta.get('images',0)>1: add('Medium','PDF contains multiple embedded images.','Avoid placing important text inside images.')
    if len(text)<400: add('High','Very little extractable text was detected.','Review the source document and parser output before relying on the score.')
    if re.search(r'(?i)\b(\d+)%\s*(skill|proficiency|expertise)',text): add('Medium','Skill/proficiency percentages detected.','Visual skill ratings can be less useful to ATS parsers than text evidence.')
    if re.search(r'(?im)^\s*(summary|experience|skills|education|projects)\s*$',text) is None: add('Medium','Conventional section headings are not consistently detectable.','Clear headings improve machine and recruiter scanning.')
    if re.search(r'(?i)\b(references available|references upon request)\b',text): add('Low','References statement detected.','Usually unnecessary unless specifically requested.')
    return issues

def score(issues):
    penalties={'Critical':30,'High':15,'Medium':7,'Low':3}; return max(0,100-sum(penalties.get(x['severity'],0) for x in issues))
