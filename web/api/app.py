from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
import shutil
import os
from schema_processor import SchemaProcessor

app = FastAPI()

# Directory to save uploaded files
upload_dir = "uploads"

# Create the upload directory if it doesn't exist
os.makedirs(upload_dir, exist_ok=True)


@app.post("/load_schema")
async def load_schema(file: UploadFile, level: int = Form(...)):

    if not file:
        return JSONResponse(content={"error": "No file uploaded"}, status_code=400)
    
    if file.content_type != "application/xml":
        return JSONResponse(content={"error": "Only XML files are allowed"}, status_code=400)
    
    # Create a unique filename for the uploaded file
    filename = os.path.join(upload_dir, file.filename)

    # Open and write the file content
    with open(filename, "wb") as f:
        shutil.copyfileobj(file.file, f)
    
    schema_processor = SchemaProcessor(filename)
    nodes = schema_processor.get_nodes_by_level(level)
    values = schema_processor.get_children_nodes(nodes)
    return {"value":values}


