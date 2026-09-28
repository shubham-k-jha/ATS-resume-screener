import json, re
from io import BytesIO
import pandas as pd
import plotly.express as px
import streamlit as st
from src.document_parser import parse_document,clean_text
from src.resume_parser import parse_resume
from src.jd_parser import parse_jd
from src.taxonomy import Taxonomy
from src.ats_checker import check
from src.scoring import evaluate
from src.recommendations import recommendations,recruiter_review
from src.jd_library import load_library
from src.exporter import to_json,to_csv
from src.config import APP_TITLE,APP_SUBTITLE,DISCLAIMER,ROLE_PROFILES
from src.resume_health import analyze_resume_health, role_likeness

st.set_page_config(page_title=APP_TITLE,page_icon='📊',layout='wide',initial_sidebar_state='expanded')

st.markdown('''<style>
.block-container{max-width:1400px;padding-top:2rem}.hero{padding:1.4rem 1.6rem;border:1px solid rgba(128,128,128,.25);border-radius:18px;background:linear-gradient(135deg,rgba(78,115,223,.12),rgba(88,214,141,.08));margin-bottom:1rem}.hero h1{margin:0}.small{opacity:.75}.metric-card{padding:1rem;border:1px solid rgba(128,128,128,.2);border-radius:14px}.tag{display:inline-block;padding:.25rem .55rem;border-radius:999px;margin:.15rem;font-size:.82rem;background:rgba(100,100,100,.12)}
</style>''',unsafe_allow_html=True)

st.markdown(f'<div class="hero"><h1>📊 {APP_TITLE}</h1><p>{APP_SUBTITLE}</p><p class="small">Understand your match. Find your gaps. Improve your resume.</p></div>',unsafe_allow_html=True)
st.caption(DISCLAIMER)

library=load_library(); tax=Taxonomy()
with st.sidebar:
    st.header('Analysis Setup')
    role=st.selectbox('Target role',list(ROLE_PROFILES.keys()),index=0)
    library_labels={'— Select —':None,**{f"{x['title']} · {x['level']}":x for x in library if role=='Custom Role' or x['role']==role}}
    chosen=st.selectbox('Representative JD',list(library_labels.keys()))
    custom_role=st.text_input('Custom role title (optional)',value='' if role!='Custom Role' else 'Data Analyst')
    st.divider(); st.subheader('Analysis options'); use_semantic=st.checkbox('Use semantic similarity when available',True); st.caption('Embeddings are optional. The app falls back to TF-IDF if the local embedding model is unavailable.')
    st.divider(); st.subheader('About'); st.write('Local-first analysis. Resume text is processed in the Streamlit session and is not sent to an external LLM by this app.')

c1,c2=st.columns(2)
with c1:
    st.subheader('1. Resume')
    resume_file=st.file_uploader('Upload PDF, DOCX, or TXT',type=['pdf','docx','txt'],key='resume')
    resume_paste=st.text_area('Or paste resume text',height=220,key='resume_text')
with c2:
    st.subheader('2. Job Description')
    jd_file=st.file_uploader('Upload PDF, DOCX, or TXT',type=['pdf','docx','txt'],key='jd')
    jd_paste=st.text_area('Or paste custom JD text',height=220,key='jd_text')
    if chosen!='— Select —' and not jd_paste and not jd_file:
        st.info('A representative sample JD is selected in the sidebar.')


def get_input(upload,paste):
    if paste.strip(): return clean_text(paste),{'type':'PASTE'}
    if upload: return parse_document(upload.getvalue(),upload.name)
    return '',{}

def score_badge(v):
    if v>=80:return '🟢'
    if v>=65:return '🟡'
    return '🔴'

if st.button('Analyze Resume',type='primary',use_container_width=True):
    try:
        rt,rm=get_input(resume_file,resume_paste); jt,jm=get_input(jd_file,jd_paste)
        if not jt.strip() and chosen!='— Select —': jt=library_labels[chosen]['description']; jm={'type':'LIBRARY','source_type':'Representative sample'}
        if not rt.strip() or not jt.strip(): st.error('Provide both a resume and a job description.'); st.stop()
        if len(rt)<80 or len(jt)<80: st.error('The resume and JD need more text for a meaningful analysis.'); st.stop()
        r=parse_resume(rt,tax); j=parse_jd(jt,tax, role if role!='Custom Role' else (custom_role or 'Custom Role')); issues=check(rt,rm,r['contact']); result=evaluate(r,j,issues,j['role']); health=analyze_resume_health(r); likeness=role_likeness(r,ROLE_PROFILES,tax); recs=recommendations(result,r,j); review=recruiter_review(result,r,j)
        st.session_state.analysis=(r,j,issues,result,recs,review,rm,jm,health,likeness)
    except Exception as e: st.error(f'Analysis failed safely: {e}')

if 'analysis' in st.session_state:
    r,j,issues,z,recs,review,rm,jm,health,likeness=st.session_state.analysis
    st.divider(); st.subheader(f"{score_badge(z['overall'])} Estimated ATS Match Score")
    st.caption(f"Target: **{j['role']}** · JD: **{j['title']}** · Semantic method: **{z['semantic_method']}**")
    cols=st.columns(5)
    for col,label,key in zip(cols,['Overall Match','ATS Formatting','JD Match','Recruiter Readiness','Required Coverage'],['overall','ats','job_match','recruiter',None]):
        val=z['overall'] if key=='overall' else z['components']['ATS Formatting'] if key=='ats' else z['job_match'] if key=='job_match' else z['recruiter'] if key=='recruiter' else z['components']['Required Skill Coverage']
        col.metric(label,f'{val:.0f}/100')

    tabs=st.tabs(['Overview','CV Health','Role Fit','Skills','JD Match','Experience','Projects','ATS Check','Recruiter Review','Recommendations','Resume Evidence'])
    with tabs[0]:
        df=pd.DataFrame({'Component':list(z['components'].keys()),'Score':list(z['components'].values())})
        st.plotly_chart(px.bar(df,x='Score',y='Component',orientation='h',range_x=[0,100],title='Score Breakdown'),use_container_width=True)
        st.info('Weights are role-aware and normalized to 100. This is a transparent analytical estimate, not an employer ATS score or hiring prediction.')
        strengths=[]
        if z['matched']: strengths.append('Direct skills: '+', '.join(z['matched'][:7]))
        if r['projects']: strengths.append('Projects provide additional technical evidence.')
        if r['metrics']: strengths.append(f'{len(r["metrics"])} measurable evidence item(s) detected.')
        st.subheader('Top strengths')
        for x in strengths[:5]: st.success(x)
        st.subheader('Why is the JD compatibility score where it is?')
        reasons=[]
        if z['missing_required']: reasons.append(f"{len(z['missing_required'])} required JD requirement(s) were not explicitly detected.")
        if z.get('evidence_gaps'): reasons.append(f"{len(z['evidence_gaps'])} requirement(s) have related evidence but not explicit wording/evidence.")
        if z['components']['Experience Match']<70: reasons.append('Experience evidence is not strongly aligned with the JD requirements.')
        if z['components']['Project Relevance']<70: reasons.append('Project evidence is not strongly aligned with the JD requirements.')
        if z['components']['ATS Formatting']<80: reasons.append('ATS formatting/parsing issues reduce the estimated match.')
        for x in reasons[:6]: st.warning(x)
        if not reasons: st.success('No major automated compatibility driver was identified.')
        st.subheader('JD-specific priority gaps')
        if z['missing_required']:
            for i,x in enumerate(z['missing_required'][:6],1): st.error(f'{i}. {x} — not detected in the resume')
        else: st.success('No missing required skills were detected by the configured taxonomy.')
        st.caption('A missing keyword means “not detected in this CV”; it does not prove the candidate lacks the underlying capability.')
    with tabs[1]:
        st.metric('Overall Resume Health',f"{health['score']:.0f}/100")
        a,b=st.columns(2)
        with a:
            st.subheader('Overall CV shortcomings')
            for x in health['shortcomings'][:10]: st.warning(x)
            if not health['shortcomings']: st.success('No major overall CV shortcomings were detected.')
        with b:
            st.subheader('CV strengths')
            for x in health['strengths'][:10]: st.success(x)
        st.dataframe(pd.DataFrame(health['checks']),hide_index=True,use_container_width=True)
        st.caption('Resume Health is independent of the selected JD: “How healthy is the CV itself?”')
    with tabs[2]:
        st.subheader('Role likeness / compatibility')
        st.caption('Evidence-based role alignment, not a hiring prediction.')
        fitdf=pd.DataFrame([{'Role':x['role'],'Role likeness':x['likeness'],'Priority skills evidenced':', '.join(x['matched_priority'][:6])} for x in likeness])
        st.plotly_chart(px.bar(fitdf.sort_values('Role likeness'),x='Role likeness',y='Role',orientation='h',range_x=[0,100],title='Role likeness from current CV evidence'),use_container_width=True)
        st.dataframe(fitdf,hide_index=True,use_container_width=True)
        st.info(f"Selected JD compatibility: **{z['job_match']:.0f}/100** · Overall CV health: **{health['score']:.0f}/100**")
    with tabs[3]:
        rows=pd.DataFrame(z['rows'])
        st.plotly_chart(px.bar(rows.sort_values('score'),x='score',y='skill',color='importance',orientation='h',range_x=[0,100],title='Required and Preferred Skill Match'),use_container_width=True)
        st.dataframe(rows[['skill','importance','match_type','score','resume_evidence','related_skills']],hide_index=True,use_container_width=True)
    with tabs[4]:
        req_rows=[x for x in z['rows'] if x['importance']=='Required']; pref_rows=[x for x in z['rows'] if x['importance']=='Preferred']
        a,b=st.columns(2); a.metric('Required covered',f"{sum(x['match_type']!='Missing' for x in req_rows)}/{len(req_rows)}"); b.metric('Preferred covered',f"{sum(x['match_type']!='Missing' for x in pref_rows)}/{len(pref_rows)}")
        st.subheader('Requirement-by-requirement evidence')
        st.dataframe(pd.DataFrame(req_rows+pref_rows)[['skill','importance','match_type','resume_evidence','related_skills']],hide_index=True,use_container_width=True)
        st.caption('Exact = explicit evidence; Related = adjacent/parent skill evidence; Missing = not detected. Missing does not establish lack of capability.')
    with tabs[5]:
        a,b=st.columns(2); a.metric('Resume years detected',r['experience_years']); b.metric('JD years requested',j['years'] or 'Not stated')
        st.metric('Experience Match',f"{z['components']['Experience Match']:.0f}/100")
        st.write('**Direct experience section:**', 'Present' if r['experience'] else 'Not detected')
        st.write('**Research/transferable evidence:**', 'Present' if r['research'] else 'Not separately detected')
    with tabs[6]:
        st.metric('Project Relevance',f"{z['components']['Project Relevance']:.0f}/100")
        st.write('Projects are assessed for technical overlap, metrics, and repository evidence.')
        st.write(r['projects'][:5000] if r['projects'] else 'No projects section detected.')
    with tabs[7]:
        st.metric('ATS Formatting Score',f"{z['components']['ATS Formatting']:.0f}/100")
        st.dataframe(pd.DataFrame(issues or [{'severity':'OK','message':'No automated formatting risk detected.','impact':'Still review the original visual document.'}]),hide_index=True,use_container_width=True)
        if rm.get('scanned_warning'): st.warning('The PDF appears to have little selectable text. OCR is not included in this local-first version.')
    with tabs[8]:
        a,b=st.columns(2)
        with a:
            st.subheader('What stands out?')
            for x in review['standout']: st.success(x)
        with b:
            st.subheader('What may cause hesitation?')
            for x in review['concerns']: st.warning(x)
        st.info(review['question']); st.caption('Evidence-based screening support, not a hiring decision.')
    with tabs[9]:
        st.subheader('Fix the CV — overall improvements')
        for x in health['shortcomings'][:8]: st.warning(x)
        st.subheader('Fix the CV — this JD')
        if recs: st.dataframe(pd.DataFrame(recs),hide_index=True,use_container_width=True)
        else: st.success('No additional automated recommendations were generated.')
        st.caption('Recommendations never instruct the candidate to claim a skill, metric, employer, project, or experience they do not genuinely have.')
    with tabs[10]:
        evidence=[x for x in z['rows'] if x['match_type'] in ('Exact','Related') and x['resume_evidence']]
        if evidence:
            for x in evidence[:20]:
                with st.expander(f"{x['skill']} · {x['match_type']}"):
                    st.write('**JD requirement:**',x['skill']); st.write('**Resume evidence:**',x['resume_evidence'])
        else: st.write('No line-level evidence was extracted for the matched skills.')

    st.divider(); st.subheader('Download Analysis')
    st.download_button('Download JSON',to_json(z,r,j,recs,review),file_name='ats_analysis.json',mime='application/json')
    st.download_button('Download Score CSV',to_csv(z),file_name='ats_score_breakdown.csv',mime='text/csv')
