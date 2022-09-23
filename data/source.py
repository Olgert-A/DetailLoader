import pandas as pd
from settings import Settings


# load detail list from file
class Source:
    def __init__(self, settings: Settings):
        self.settings = settings

    def load(self) -> list:
        file = self.settings.source.file
        sheet = self.settings.source.sheet
        column = self.settings.source.column
        table = pd.read_excel(io=file, sheet_name=sheet, header=None)
        return table[column].astype(str).tolist()
