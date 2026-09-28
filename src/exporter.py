import io,json
import pandas as pd

def to_json(result,resume,jd,recs,review):
    return json.dumps({'analysis':result,'resume_contact':resume['contact'],'job_description':{'role':jd['role'],'title':jd['title']},'recommendations':recs,'recruiter_review':review},indent=2,default=str)

def to_csv(result):
    return pd.DataFrame([{'component':k,'score':v,'weight':result['weights'].get(_weight_key(k),0)} for k,v in result['components'].items()]).to_csv(index=False).encode()

def _weight_key(k):
    return {'Skill Match':'skill_match','Required Skill Coverage':'required_coverage','Semantic JD Match':'semantic_match','Experience Match':'experience_match','Project Relevance':'project_relevance','Tools/Technology Match':'tools_match','Education Match':'education_match','Achievement Evidence':'achievement_evidence','Communication':'communication','Presentation':'presentation','English/Language Quality':'language_quality','ATS Formatting':'ats_formatting'}.get(k,'')
