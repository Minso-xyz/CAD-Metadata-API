# CAD Metadata API
 
A FastAPI backend that analyzes STEP files using an existing C# STEP analysis engine.
 
## Overview
 
The API accepts a STEP file upload, invokes the STEPInspector CLI,
and returns extracted CAD metadata as JSON.
 
## Architecture
 
Client
↓
FastAPI
↓
Temporary STEP File
↓
STEPInspector.CLI
↓
StepAnalyzer
↓
JSON
↓
FastAPI Response
 
## Current Features
- Upload `.step` and `.stp` files
- Validate STEP file extensions
- Store uploaded files temporarily
- Invoke the C# STEPInspector CLI from Python
- Pass STEP file paths through command-line arguments
- Receive analysis results as JSON
- Configure the CLI location using an environment variable
 
## Tech Stack
- Python
- FastAPI
- Pydantic
- C#
- .NET 8
- REST API
 
## Status
 
Work in progress
 
Currently working on:
- Parsing CLI JSON output into structured API responses
- Error handling
- Automated tests
- Temporary file cleanup
