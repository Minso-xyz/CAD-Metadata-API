from fastapi import FastAPI, UploadFile, HTTPException
from pydantic import BaseModel
import tempfile
import os
import subprocess

CLI_DIR = os.getenv("STEPINSPECTOR_CLI_DIR")
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

    result = subprocess.run([os.path.join(CLI_DIR, "STEPInspector.CLI.exe"),    # Program to execute
                             temp_file_path],    # args[0]  (step file path + step file name)
                             capture_output=True, 
                             text=True,
                             cwd=CLI_DIR)
    
    return {
        "file_name": file.filename,
        "status": "Received",
        "temp_path": temp_file_path,
        "cli_output": result.stdout,
        "cli_error": result.stderr,
        "cli_return_code": result.returncode
        }