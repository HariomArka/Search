import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

with open("app/data/problems.json") as f:
    problems = json.load(f)

titles = [p["title"] + " " + " ".join(p["topics"]) for p in problems]
vectorizer = TfidfVectorizer().fit(titles)
vectors = vectorizer.transform(titles)

def search_problems(query, k=30):
    query_vec = vectorizer.transform([query])
    scores = cosine_similarity(query_vec, vectors)[0]
    top_k_indices = scores.argsort()[::-1][:k]
    return [problems[i] for i in top_k_indices if scores[i] > 0.1]
