from twttr import shorten


def test_upper_lower():
    assert shorten("HelLO") == "HlL"
    assert shorten("WoRlD") == "WRlD"


def test_number():
    assert shorten("12345") == "12345"


def test_punctuation():
    assert shorten(";',.:@") == ";',.:@"
