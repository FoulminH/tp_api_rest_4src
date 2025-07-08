from fastapi import FastAPI
from routers import all_routers
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello this is the API for mysql"}

for router in all_routers:
    app.include_router(router)
