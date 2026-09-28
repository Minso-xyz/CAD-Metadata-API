from fastapi import FastAPI, UploadFile, HTTPException
from pydantic import BaseModel
import tempfile
import os

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
    
    content = await file.read()

    temp_dir = tempfile.gettempdir()
    temp_file_path = os.path.join(temp_dir, file.filename)

    with open(temp_file_path, "wb") as temp_file:   # binary write mode
        temp_file.write(content)
    
    return {
        "file_name": file.filename,
        "status": "Received",
        "temp_path": temp_file_path
    }