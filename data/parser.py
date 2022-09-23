from settings import Settings


# parse loader information
class Parser:
    def __init__(self, settings: Settings):
        self.settings = settings

    def parse(self, raw: dict) -> dict:
        return raw
