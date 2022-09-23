from settings import Settings


# load information for each detail in list and return html data
class Loader:
    def __init__(self, settings: Settings):
        self.settings = settings

    async def load(self, detail_list: list) -> dict:
        return {detail: '' for detail in detail_list}
