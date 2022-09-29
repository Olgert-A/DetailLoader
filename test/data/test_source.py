from settings import Settings
from data.source import Source


def test_source():
    settings = Settings(r'.\test\settings.json')
    assert settings.status

    source = Source(settings)
    detail_list = source.load()
    assert detail_list == ['Pin 193', 'Pin 205']

