from fastapi import FastAPI, UploadFile, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Metadata(BaseModel):
    file_name: str
    entity_count: int

@app.get("/health")
def health():
    return {"status" : "healthy"}

@app.post("/metadata")
def create_metadata(metadata: Metadata):
    return {
        "message": "Metadata received",
        "file_name":metadata.file_name,
        "entity_count": metadata.entity_count
        }

@app.post("/api/step/analyze")
async def analyze_step(file: UploadFile):

    if not file.filename.lower().endswith((".step", ".stp")):
        raise HTTPException(
            status_code=400,
            detail="ONLY STEP files (.step, .stp) are supported."
        )
    
    return {
        "file_name": file.filename,
        "status": "Received"
    }