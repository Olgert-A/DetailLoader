import asyncio

from settings import Settings
from data.source import Source
from data.loader import Loader
from data.parser import Parser
from data.result import Result


async def main():
    settings = Settings('settings.json')
    if not settings.status:
        print('Error loading settings')
        return

    source = Source(settings)
    loader = Loader(settings)
    parser = Parser(settings)
    result = Result(settings)

    print('Detail list loading...')
    detail_list = source.load()
    print('Detail list loaded successful')

    print('Detail raw info loading...')
    raw = await loader.load(detail_list)
    print('Detail raw info loaded successful')

    print('Detail info parsing...')
    parsed = parser.parse(raw)
    print('Detail info parsed successful')

    print('Detail info saving...')
    result.save(parsed)
    print('Detail info saved successful')

if __name__ == '__main__':
    asyncio.run(main())

