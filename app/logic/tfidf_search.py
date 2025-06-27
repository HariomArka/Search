# import json
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# with open("./data/all_problems.json") as f:
#     problems = json.load(f)

# titles = [p["title"] + " " + " ".join(p["topics"]) for p in problems]
# vectorizer = TfidfVectorizer().fit(titles)
# vectors = vectorizer.transform(titles)

# def search_problems(query, k=30):
#     query_vec = vectorizer.transform([query])
#     scores = cosine_similarity(query_vec, vectors)[0]
#     top_k_indices = scores.argsort()[::-1][:k]
#     return [problems[i] for i in top_k_indices if scores[i] > 0.1]


# import json
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# import os

# # Resolve paths
# base_dir = os.path.dirname(os.path.abspath(__file__))
# file1 = os.path.join(base_dir, "./data/problems.json")
# file2 = os.path.join(base_dir, "app/data/all_problems.json")

# # Load both files
# with open(file1, encoding="utf-8") as f1, open(file2, encoding="utf-8") as f2:
#     problems1 = json.load(f1)
#     problems2 = json.load(f2)

# # Merge and deduplicate (optional)
# problems = problems1 + problems2

# # Prepare data for TF-IDF
# titles = [p["title"] + " " + " ".join(p.get("topics", [])) for p in problems]
# vectorizer = TfidfVectorizer().fit(titles)
# vectors = vectorizer.transform(titles)

# # Search function
# def search_problems(query, k=30):
#     query_vec = vectorizer.transform([query])
#     scores = cosine_similarity(query_vec, vectors)[0]
#     top_k_indices = scores.argsort()[::-1][:k]
#     return [problems[i] for i in top_k_indices if scores[i] > 0.1]


import os
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Get the base project directory
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Correct file paths
file1 = os.path.join(base_dir, "data", "problems.json")
file2 = os.path.join(base_dir, "data", "all_problems.json")

# Load files
with open(file1, encoding="utf-8") as f1, open(file2, encoding="utf-8") as f2:
    problems1 = json.load(f1)
    problems2 = json.load(f2)

# Combine
problems = problems1 + problems2

# Vectorize
titles = [p["title"] + " " + " ".join(p.get("topics", [])) for p in problems]
vectorizer = TfidfVectorizer().fit(titles)
vectors = vectorizer.transform(titles)

def search_problems(query, k=30):
    query_vec = vectorizer.transform([query])
    scores = cosine_similarity(query_vec, vectors)[0]
    top_k_indices = scores.argsort()[::-1][:k]
    return [problems[i] for i in top_k_indices if scores[i] > 0.1]
