from fastapi import APIRouter, Query
from app.logic.tfidf_search import search_problems

router = APIRouter()

@router.get("/search")
def get_problems(query: str = Query(...)):
    return {"results": search_problems(query)}
