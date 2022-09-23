from settings import Settings


# load detail list from file
class Source:
    def __init__(self, settings: Settings):
        self.settings = settings

    def load(self) -> list:
        return []
