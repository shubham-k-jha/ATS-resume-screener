from src.taxonomy import Taxonomy
from src.resume_parser import parse_resume
from src.jd_parser import parse_jd
from src.ats_checker import check
from src.scoring import evaluate

def sample_resume():
    return '''Shubham Jha\nshubham@example.com | +91 9876543210\nhttps://github.com/example\n\nSUMMARY\nData analyst transitioning from scientific research with Python, SQL and Power BI experience.\n\nSKILLS\nPython, SQL, PostgreSQL, MySQL, Pandas, Power BI, Plotly, Statistics, Git\n\nEXPERIENCE\nResearch Analyst\n3 years of scientific data analysis and time-series modeling.\n\nPROJECTS\nBuilt an interactive Power BI dashboard and SQL analysis for sales KPIs.\n\nEDUCATION\nM.Sc. Physics\n'''

def test_taxonomy_aliases():
    t=Taxonomy(); found=t.find('Postgres, PowerBI, sklearn, ML and MS Excel')
    assert {'PostgreSQL','Power BI','scikit-learn','Machine Learning','Excel'} <= set(found)

def test_resume_sections_and_contacts():
    r=parse_resume(sample_resume())
    assert r['contact']['email']=='shubham@example.com'
    assert r['experience_years']==3
    assert 'Power BI' in r['skills']
    assert r['projects']

def test_required_preferred_classification():
    t=Taxonomy(); j=parse_jd('Data Analyst\nRequired: SQL, Power BI, Python\nPreferred: Tableau, AWS',t,'Data Analyst')
    assert 'SQL' in j['required'] and 'Tableau' in j['preferred']

def test_score_range_and_gaps():
    t=Taxonomy(); r=parse_resume(sample_resume(),t); j=parse_jd('Data Analyst\nRequired: SQL, Power BI, Tableau\nPreferred: Python',t,'Data Analyst')
    z=evaluate(r,j,check(r['raw'],{},r['contact']),'Data Analyst')
    assert 0 <= z['overall'] <= 100
    assert 'Tableau' in z['missing_required']

def test_empty_format_risk():
    issues=check('short',{}, {'email':'','phone':''})
    assert any(x['severity']=='Critical' for x in issues)

def test_inline_library_style_required_preferred():
    t=Taxonomy(); j=parse_jd('Data Analyst. Required: SQL, Python, Power BI. Preferred: Tableau, AWS. 2+ years.',t,'Data Analyst')
    assert {'SQL','Python','Power BI'} <= j['required']
    assert {'Tableau','AWS'} <= j['preferred']
    assert j['years']==2
