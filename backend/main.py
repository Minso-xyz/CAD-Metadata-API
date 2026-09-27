from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Metadata(BaseModel):
    file_name: str
    entity_count: int

@app.get("/health")
def health():
    return {"status" : "healthy"}

@app.get("/unhealth")
def unhealth():
    return {"status" : "unhealthy"}

@app.post("/metadata")
def create_metadata(metadata: Metadata):
    return {
        "message": "Metadata received",
        "file_name":metadata.file_name,
        "entity_count": metadata.entity_count
        }