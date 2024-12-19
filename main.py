from fastapi import FastAPI, File, UploadFile
from typing import Annotated
from dotenv import load_dotenv
import requests
import os

load_dotenv()

apikey = os.getenv("DB_APIKEY")
urlScan = os.getenv("DB_URLSCAN")
urlReport = os.getenv("DB_URLREPORT")

app = FastAPI()

# http://localhost:8000
@app.get("/")
def index():
    return {"message" : "File Malware Scanner Challenge"}

@app.post("/scanner")
async def scanning_file(file: Annotated[UploadFile, File(description="Scanning with VirusTotal")],):
    myfile = open(file.filename, 'wb')
    content = await file.read()
    myfile.write(content)
    myfile.close()
    files = {'file': (file.filename, open(file.filename, 'rb'))}
    response = requests.post(urlScan, files=files, params={'apikey': apikey}).json()

    print(f"Escaneando {file.filename} ...")
    print(response['verbose_msg'])

    return {"response" : response }

@app.get("/report/{resourceScan}")
async def report_of_scanning_file(resourceScan: str):
    responseget = requests.get(urlReport, params={'apikey': apikey, 'resource' : resourceScan}).json()
    print(f"Fecha de escaneo: {responseget['scan_date']}")
    print(f"Se encontraron {responseget['positives']} virus")
    print(responseget['verbose_msg'])

    return {"response" : responseget }

# http://localhost:8000/docs