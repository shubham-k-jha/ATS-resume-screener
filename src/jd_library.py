import json
from pathlib import Path

def load_library():
    p=Path(__file__).parents[1]/'data/job_descriptions/library.json'; return json.loads(p.read_text(encoding='utf-8'))
