import logging
import pandas as pd
from settings import Settings


# parse loader information
class Parser:
    def __init__(self, settings: Settings):
        self.settings = settings

    def parse(self, raw: dict) -> dict:
        return {detail: self.parse_detail(detail, html_data)
                for detail, html_data in raw.items()}

    def parse_detail(self, detail: str, html_data: str) -> list:
        tables = pd.read_html(io=html_data)
        if not len(tables):
            logging.info(f'{detail} data not found!')
            return []

        df = tables[0]
        print(df)

        # get column without nan
        col = 'Detail'

        # get index of not null elements in col
        dind = df.index[df[col].notnull()].tolist()
        dind.append(df.index[-1])

        return ['data']

