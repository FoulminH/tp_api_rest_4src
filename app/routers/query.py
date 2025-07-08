from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, constr
import db
import re

router = APIRouter()

class SQLQuery(BaseModel):
    query: constr(min_length=1)


@router.post("/query")
async def query(payload: SQLQuery):
    query = payload.query.strip()
    
    if not is_select_query(query=query):
        raise HTTPException(status_code=400, detail="Only SELECT query are allowed")



def is_select_query(query: str) -> bool:
    pattern = r'^\s*select'
    return re.match(pattern=pattern, string=query, flags=re.IGNORECASE) is not None
    
    