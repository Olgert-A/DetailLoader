import pandas as pd
from settings import Settings


# save results to file
class Result:
    def __init__(self, settings: Settings):
        self.settings = settings

    def save(self, parsed: dict) -> None:
        data_to_frame = [(dse, part_of, product, amount)
                         for dse, data in parsed.items()
                         for part_of, product, amount in data
                         if data]
        result = pd.DataFrame.from_records(data_to_frame, columns=['Detail', 'Part of', 'Product', 'Amount'])
        result_file = self.settings.result.file
        result.to_excel(result_file, index=False)
