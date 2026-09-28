def recommendations(result,resume,jd):
    out=[]
    for s in result['missing_required'][:8]:
        out.append({'priority':'HIGH','item':s,'action':f'First verify whether you genuinely have {s}. If yes, surface the existing evidence in the summary, skills, experience, or project bullets. If not, do not add it merely for ATS matching.'})
    for s in result.get('evidence_gaps',[])[:5]:
        out.append({'priority':'HIGH','item':f'{s} — evidence gap','action':f'Relate your existing experience to {s} only where the connection is truthful, then add concrete evidence rather than just the keyword.'})
    if not resume['sections']['summary']: out.append({'priority':'HIGH','item':'Professional summary','action':'Add a concise role-targeted summary using only verified skills, experience, and projects.'})
    if not resume['projects']: out.append({'priority':'HIGH','item':'Projects','action':'Add relevant projects with problem, data, tools, methods, results, and a repository/portfolio link when genuinely available.'})
    if len(resume['metrics'])<2: out.append({'priority':'MEDIUM','item':'Achievement evidence','action':'Strengthen bullets with truthful measurable outcomes such as records processed, accuracy, scale, time saved, or impact. Never invent numbers.'})
    if not resume['contact']['linkedin']: out.append({'priority':'MEDIUM','item':'LinkedIn','action':'Add a clean LinkedIn URL if you actively use one.'})
    if not resume['contact']['github'] and jd['all'] & {'Git','GitHub'}: out.append({'priority':'MEDIUM','item':'GitHub evidence','action':'Add GitHub only if it contains genuine, relevant work.'})
    for s in result['missing_preferred'][:5]: out.append({'priority':'LOW','item':s,'action':f'Optional: demonstrate {s} only if it is a real capability or genuine project experience.'})
    return out

def recruiter_review(result,resume,jd):
    strengths=[]
    if result['matched']: strengths.append('Direct evidence for '+', '.join(result['matched'][:5]))
    if resume['projects']: strengths.append('Projects section provides additional evidence')
    if resume['experience']: strengths.append('Professional/research experience is available for review')
    if resume['metrics']: strengths.append('Some quantified evidence is present')
    concerns=[]
    if result['missing_required']: concerns.append('Required JD skills are missing or not evidenced: '+', '.join(result['missing_required'][:5]))
    if result.get('evidence_gaps'): concerns.append('Some requirements have related evidence but not explicit wording: '+', '.join(result['evidence_gaps'][:5]))
    if result['components']['ATS Formatting']<80: concerns.append('ATS formatting/parsing risks need review')
    if result['components']['Experience Match']<60: concerns.append('Relevant experience evidence is limited or indirect')
    if result['components']['Project Relevance']<60: concerns.append('Project evidence is limited for this JD')
    target=jd.get('role') or 'Custom role'
    return {'target':target,'standout':strengths[:5] or ['No strong evidence identified by the automated checks.'],'concerns':concerns[:5] or ['No major automated concern identified.'],'question':'Would a recruiter understand the candidate target role within the first screen? Review the summary, recent experience, skills, and first two projects together.'}
