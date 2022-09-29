import pandas as pd
from settings import Settings
from data.result import Result


def test_result():
    settings = Settings(r'.\test\settings.json')
    assert settings.status

    # data to save
    parsed = {'Pin 193': [('Engine', 'Auto', 8.0), ('Wheel', 'Moto', 4.0)]}

    # save data
    result = Result(settings)
    result.save(parsed)

    # load parsed to pandas.DataFrame
    converters = {'Detail': str, 'Part of': str, 'Product': str, 'Amount': float}
    from_excel = pd.read_excel(settings.result.file, converters=converters)

    # convert 'parsed' to pandas.DataFrame using 'to_frame'
    to_frame = [(detail, part_of, product, amount)
                for detail, data in parsed.items()
                for part_of, product, amount in data]

    parsed_frame = pd.DataFrame.from_records(to_frame, columns=converters.keys())

    # check identity
    assert parsed_frame.equals(from_excel)
