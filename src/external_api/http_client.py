
import aiohttp
from aiohttp import ClientResponseError
from starlette.responses import JSONResponse

from src.external_api.config import API_KEY, API_URL
headers = {"X-CMC_PRO_API_KEY": API_KEY}


async def get_all_currencies():
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(API_URL + "/v1/cryptocurrency/listings/latest", headers=headers) as response:
                response.raise_for_status()
                data = await response.json()
                return data["data"]
        except ClientResponseError as er:
            return {"message": "something went wrong(", "detail": er}
async def get_currency(id: int):
    async with aiohttp.ClientSession() as session:
        try:
            async  with session.get(API_URL + "/v2/cryptocurrency/quotes/latest", headers=headers, params={"id": id}) as response:
                response.raise_for_status()
                data = await response.json()
                return data["data"][str(id)]
        except ClientResponseError as er:
            return {"message": "something went wrong(", "detail": er}




