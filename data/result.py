from settings import Settings


# save results to file
class Result:
    def __init__(self, settings: Settings):
        self.settings = settings

    def save(self, parsed: dict) -> None:
        pass
