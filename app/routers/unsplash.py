import os
from fastapi import Request, APIRouter, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests

from dotenv import load_dotenv
load_dotenv()

templates = Jinja2Templates(directory="templates")

router = APIRouter()
key = os.getenv("unsplash_token")


@router.get("/unsplash", response_class=HTMLResponse)
async def unsplash_home(request: Request):
    img = requests.get("https://api.unsplash.com/photos/Na0BbqKbfAo?client_id="+key)
    thumb=img.json()["urls"]["regular"]
    return templates.TemplateResponse("unsplash.html", {"request": request, "key": key, "thumbnail": thumb})
