from fastapi import FastAPI, Request
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

import os

import uvicorn

# import veoplay as xml_content
from service import get_all_data, createXML


path = os.path.dirname(os.path.realpath(__file__))

app = FastAPI(
    title='SPORT PL APP',
    description='Parsing data from https://viaplay.pl/sport',
    version='1.0.0',
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

headers = {'Content-Type': 'application/xml'}

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse('index.html', {"request": request,})



@app.get("/sport.xml")
def xml_endpoint(request: Request):
    createXML(get_all_data())
    with open(f'{path}/sport.xml', 'r') as xml_file:
        xml = xml_file.read()
        xml_file.close()

    response = Response(content=xml, media_type="application/xml")
    return response


if __name__ == '__main__':
    uvicorn.run('main:app',
                reload=True,
                host='0.0.0.0', 
                port=5000)