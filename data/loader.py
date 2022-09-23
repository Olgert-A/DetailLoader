import aiohttp
import asyncio
import urllib.parse
from settings import Settings


# load information for each detail in list and return html data
class Loader:
    def __init__(self, settings: Settings):
        self.settings = settings

    async def load(self, detail_list: list) -> dict:
        # set connections limit
        connector = aiohttp.TCPConnector(limit=50)
        # open session and run tasks
        async with aiohttp.ClientSession(connector=connector) as session:
            tasks = [self.load_detail(session, detail) for detail in detail_list]
            task_result = await asyncio.gather(*[asyncio.create_task(t) for t in tasks])
            return {detail: html_data for detail, html_data in task_result}

    async def load_detail(self, session, detail) -> tuple:
        url = self.get_detail_url(detail)
        async with session.get(url) as response:
            status = response.status
            text = await response.text()
            encoding = response.get_encoding()

            if status == 200:
                # decode from site encoding to cp1251
                return detail, text.encode(encoding).decode('cp1251')
            else:
                return detail, ''

    def get_detail_url(self, detail):
        url = self.settings.site.url
        detail = urllib.parse.quote(detail, encoding='cp1251')
        return f"{url}{detail}"
