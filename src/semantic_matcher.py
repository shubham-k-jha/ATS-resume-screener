from functools import lru_cache
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

@lru_cache(maxsize=1)
def _embedding_model():
    try:
        from sentence_transformers import SentenceTransformer
        return SentenceTransformer('all-MiniLM-L6-v2')
    except Exception:
        return None

def similarity(a,b):
    a=(a or '').strip(); b=(b or '').strip()
    if not a or not b:return 0.0,'unavailable'
    m=_embedding_model()
    if m:
        v=m.encode([a,b],normalize_embeddings=True); return float(v[0]@v[1]),'sentence-transformer'
    try:
        v=TfidfVectorizer(stop_words='english',ngram_range=(1,2),max_features=5000).fit_transform([a,b])
        return float(cosine_similarity(v[0],v[1])[0,0]),'tf-idf'
    except ValueError:return 0.0,'unavailable'

def requirement_similarity(requirement,evidence): return similarity(requirement,evidence)[0]
