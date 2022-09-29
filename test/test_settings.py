from settings import Settings


def test_settings():
    s = Settings(r'.\test\settings.json')
    assert s.status
    assert s.source.file == ".\\test\\source.xlsx"
    assert s.source.sheet == "Лист1"
    assert s.source.column == 0
    assert s.result.file == "result.xlsx"
    assert s.site.url == "http://127.0.0.1:8000/"
