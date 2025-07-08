from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
import db

router = APIRouter()

@router.get("/status")
def status():
    with db.Database() as (connection, cursor):
        cursor.execute("SHOW GLOBAL STATUS")
        raw_status = cursor.fetchall()
        status = {item["Variable_name"]: int(item["Value"]) if item["Value"].isdigit() else item["Value"] 
              for item in raw_status}
        
        cursor.execute("SELECT VERSION();")
        version_raw = cursor.fetchall()
        
        version = jsonable_encoder(version_raw[0]["VERSION()"])
        
    return {
        "status": status,
            "version": version
    }