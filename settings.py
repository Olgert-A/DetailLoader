import json
import logging


class Settings:
    class Source:
        def __init__(self, file: str, sheet: str, column: int):
            self.file = file
            self.sheet = sheet
            self.column = column

    class Result:
        def __init__(self, file: str):
            self.file = file

    class WebSite:
        def __init__(self, url: str):
            self.url = url

    def __init__(self, file):
        self.source: Settings.Source
        self.result: Settings.Result
        self.site: Settings.WebSite
        self.status = self.load(file)

    def load(self, file):
        result = False

        with open(file, encoding='cp1251') as f:
            try:
                data = json.load(f)

                file = data['source']['file']
                sheet = data['source']['sheet']
                column = data['source']['column']
                self.source = Settings.Source(file, sheet, column)

                file = data['result']['file']
                self.result = Settings.Result(file)

                url = data['site']['url']
                self.site = Settings.WebSite(url)
                result = True
            except ValueError:
                logging.exception('Error loading script settings')

        return result
