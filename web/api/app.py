from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
import shutil
import os
import uuid
from schema_processor import SchemaProcessor
from xml_processor import XMLProcessor
from pydantic import BaseModel
from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI()

# Directory to save uploaded files
upload_dir = "uploads"

# Create the upload directory if it doesn't exist
os.makedirs(upload_dir, exist_ok=True)


class XmlSearchQuery(BaseModel):
    filename: str
    query: str = None
    filters: list = []
    enums: list = []
    is_case_sensitive: bool = False
    fuzzy_level: int = 8


@app.post("/load_schema")
async def load_schema(file: UploadFile, level: int = Form(...)):
    try:
        if not file:
            return JSONResponse(content={"error": "No file uploaded"}, status_code=400)

        if file.content_type != "application/xml":
            return JSONResponse(content={"error": "Only XSD files are allowed"}, status_code=400)

        # Generate a unique identifier
        unique_id = str(uuid.uuid4())

        # Get the file's extension
        file_extension = os.path.splitext(file.filename)[1]

        # Create a unique filename by combining the identifier and extension
        unique_filename = f"{unique_id}{file_extension}"

        # Save the file with the unique filename
        filename = os.path.join(upload_dir, unique_filename)

        # Open and write the file content
        with open(filename, "wb") as f:
            shutil.copyfileobj(file.file, f)

        schema_processor = SchemaProcessor(filename)
        nodes = schema_processor.get_nodes_by_level(level)
        values = schema_processor.get_children_nodes(nodes)
        return {"value": values}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/load_xml")
async def load_xml(file: UploadFile):
    try:
        if not file:
            return JSONResponse(content={"error": "No file uploaded"}, status_code=400)

        if file.content_type != "application/xml":
            return JSONResponse(content={"error": "Only XSD files are allowed"}, status_code=400)

        # Generate a unique identifier
        unique_id = str(uuid.uuid4())

        # Get the file's extension
        file_extension = os.path.splitext(file.filename)[1]

        # Create a unique filename by combining the identifier and extension
        unique_filename = f"{unique_id}{file_extension}"

        # Save the file with the unique filename
        filename = os.path.join(upload_dir, unique_filename)

        # Open and write the file content
        with open(filename, "wb") as f:
            shutil.copyfileobj(file.file, f)

        return {"filename": unique_id}

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/get_xml_content")
def get_xml_content(search_query: XmlSearchQuery):
    try:
        file_path = os.path.join(upload_dir, f"{search_query.filename}.xml")

        with open(file_path, "rb") as file:
            xml_processor = XMLProcessor(file)
            results = xml_processor.query_xml(
                search_query.query, search_query.filters, search_query.enums, search_query.is_case_sensitive, search_query.fuzzy_level)
            return {"value": results}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
