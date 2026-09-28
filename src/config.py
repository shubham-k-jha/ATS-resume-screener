APP_TITLE='ATS Resume Screener'
APP_SUBTITLE='Recruiter-grade Resume × Job Description Intelligence'
DISCLAIMER='Estimated ATS Match Score — an analytical estimate, not an official employer ATS score or hiring decision.'

BASE_WEIGHTS={
 'skill_match':22,'required_coverage':18,'semantic_match':12,'experience_match':10,
 'project_relevance':8,'tools_match':8,'education_match':4,'achievement_evidence':5,
 'communication':4,'presentation':2,'language_quality':2,'ats_formatting':5}

ROLE_PROFILES={
 'Data Analyst': {'priority':['SQL','Excel','Power BI','Tableau','Python','Pandas','Data Cleaning','Statistics','Data Visualization','Reporting','KPI Analysis','Business Communication']},
 'Data Scientist': {'priority':['Python','SQL','Statistics','Machine Learning','scikit-learn','Pandas','NumPy','Feature Engineering','Model Evaluation','Experimentation','Git']},
 'Business Analyst': {'priority':['SQL','Excel','Power BI','Requirements Gathering','Stakeholder Management','KPI Analysis','Reporting','Business Analysis','Process Improvement']},
 'BI Analyst': {'priority':['SQL','Power BI','Tableau','DAX','ETL','Data Modeling','Dashboarding','KPI Analysis']},
 'Product Analyst': {'priority':['SQL','Python','Product Analytics','Funnel Analysis','Cohort Analysis','Retention','A/B Testing','Experimentation','Product KPIs']},
 'Marketing Analyst': {'priority':['SQL','Python','Excel','Google Analytics','Marketing Analytics','Campaign Analysis','Conversion Rate','ROI','Attribution','Dashboarding']},
 'Financial Data Analyst': {'priority':['SQL','Excel','Python','Financial Analysis','Forecasting','Reporting','KPI Analysis','Power BI']},
 'Operations Analyst': {'priority':['SQL','Excel','Python','Process Improvement','KPI Analysis','Reporting','Dashboarding','Statistics']},
 'Reporting Analyst': {'priority':['SQL','Excel','Power BI','Reporting','Dashboarding','KPI Analysis','Data Visualization']},
 'Junior Data Scientist': {'priority':['Python','SQL','Statistics','Machine Learning','scikit-learn','Pandas','NumPy','EDA','Model Evaluation']},
 'Associate Data Scientist': {'priority':['Python','SQL','Machine Learning','Statistics','Feature Engineering','Model Evaluation','scikit-learn','Git']},
 'Machine Learning Analyst': {'priority':['Python','SQL','Machine Learning','Statistics','scikit-learn','Feature Engineering','Model Evaluation']},
 'Analytics Engineer': {'priority':['SQL','Python','dbt','ETL','Data Modeling','Git','Airflow','Cloud']},
 'Custom Role': {'priority':[]}
}
