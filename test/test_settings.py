from settings import Settings


def test_settings():
    s = Settings(r'.\test\settings.json')
    assert s.status
    assert s.source.file == ".\\test\\source.xlsx"
    assert s.source.sheet == "Лист1"
    assert s.source.column == 2
    assert s.result.file == "result.xlsx"
    assert s.site.url == "localhost:8080"
