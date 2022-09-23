from settings import Settings
from data.source import Source


def test_source():
    settings = Settings(r'.\test\settings.json')
    assert settings.status

    source = Source(settings)
    detail_list = source.load()
    print(detail_list)
    assert len(detail_list) > 0
