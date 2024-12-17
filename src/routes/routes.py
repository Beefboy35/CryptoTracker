from fastapi import APIRouter,  Request

from fastapi.templating import Jinja2Templates

from src.external_api.http_client import get_all_currencies, get_currency

ext_api = APIRouter()

templates = Jinja2Templates(directory="templates")
@ext_api.get("/list")
async def get_currency_list(req: Request):
    return templates.TemplateResponse(req, "list.html",{"crypto": await get_all_currencies()})


@ext_api.get("/curr/{id}")
async def get_curr(id: int, req: Request):
    return  templates.TemplateResponse(req, "currency.html", {"data": await get_currency(id)})
