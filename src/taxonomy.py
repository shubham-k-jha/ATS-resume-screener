import json,re
from pathlib import Path

class Taxonomy:
    def __init__(self,path=None):
        p=Path(path) if path else Path(__file__).parents[1]/'data/skills/skill_taxonomy.json'
        self.skills=json.loads(p.read_text(encoding='utf-8'))['skills']
        self.alias={}
        for item in self.skills:
            for term in [item['name'],*item.get('synonyms',[])]: self.alias[term.lower()]=item['name']
        self.by_name={x['name']:x for x in self.skills}
    def find(self,text):
        out={}
        for alias,name in self.alias.items():
            pattern=r'(?<![A-Za-z0-9+#])'+re.escape(alias)+r'(?![A-Za-z0-9+#])'
            if re.search(pattern,text,re.I): out[name]=self.by_name[name]
        return out
    def normalize(self,skills): return {self.alias.get(s.lower(),s) for s in skills}
