import logging
import pandas as pd
from collections import namedtuple
from settings import Settings


# parse loader information
class Parser:
    def __init__(self, settings: Settings):
        self.settings = settings
        self.details_with_errors = []

    def parse(self, raw: dict) -> dict:
        """
        Parse all details.
        :param raw: dict with detail and search results html strings
        :return: dict with detail and detail usage list
        """
        return {detail: self.parse_detail(detail, html_data)
                for detail, html_data in raw.items()}

    def parse_detail(self, detail: str, html_data: str) -> list:
        """
        Parse one detail.
        :param detail: detail name
        :param html_data: string with html with search results
        :return: detail usage list with tuples (part_of, product, amount)"
        """
        search_data = self.read_table(detail, html_data)
        if search_data.empty:
            return []

        detail_raw = self.slice_detail(detail, search_data)
        if detail_raw.empty:
            return []

        return self._extract_data(detail_raw)

    def read_table(self, detail: str, html_data: str) -> pd.DataFrame:
        """
        Load search result html to DataFrame
        :param detail: detail name
        :param html_data: html data to load
        :return: DataFrame with table of search results
        """
        tables = pd.read_html(io=html_data)
        if not len(tables):
            self.details_with_errors.append(detail)
            print(log := f'{detail} - html data not found!')
            logging.info(log)
            return pd.DataFrame()
        return tables[0]

    def slice_detail(self, detail: str, search_result: pd.DataFrame) -> pd.DataFrame:
        """
        Find detail data with status Active in search_result
        :param detail: Detail name
        :param search_result: DataFrame contain raw search results loaded from html
        :return: DataFrame sliced by detail and status
        """
        # slice search_result by detail name to find detail info
        detail_frame = Parser._slice(detail, 'Detail', search_result)
        if detail_frame.empty:
            self.details_with_errors.append(detail)
            print(log := f'{detail} info not found!')
            logging.info(log)
            return pd.DataFrame()

        # slice detail info by status to find active
        active_frame = Parser._slice('Active', 'Status', detail_frame)
        if active_frame.empty:
            self.details_with_errors.append(detail)
            print(log := f'{detail} active data not found!')
            logging.info(log)
            return pd.DataFrame()

        return active_frame

    @staticmethod
    def _slice(by_value: str, column: str, table: pd.DataFrame) -> pd.DataFrame:
        """
        Find search_value in column and slice DataFrame from search_value to next not null value
        :param by_value: Value will be searched
        :param column: Column used as search target
        :param table: DataFrame to slice
        :return: Sliced DataFrame
        """
        Item = namedtuple('Item', 'value index')
        row_amount, _ = table.shape
        # clear nan rows in column
        data = table[table[column].notnull()]
        # create index-value pair
        pairs = [Item(row[column], index) for index, row in data.iterrows()]
        # add rows amount to last element as index to slice last interval
        pairs.append(Item('row_amount', row_amount))
        # find value and get index of next value to slice range with data
        for i in range(len(pairs)-1):
            if pairs[i].value == by_value:
                start, end = pairs[i].index, pairs[i+1].index
                return table.iloc[start:end]

        return pd.DataFrame()

    @staticmethod
    def _extract_data(detail_raw: pd.DataFrame) -> list:
        """
        Extract detail data to detail usage list. Extract is not include first row which contains only status.
        :param detail_raw: sliced DataFrame contains detail data with status Active
        :return: list of tuples (part_of, product, amount)
        """
        return [(detail_raw.at[index, 'Part_of'],
                 detail_raw.at[index, 'Product'],
                 detail_raw.at[index, 'Amount'])
                for index, row in detail_raw.iterrows()
                if index != detail_raw.index[0]]
