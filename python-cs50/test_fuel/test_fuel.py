from fuel import convert, gauge
import pytest

def main():

    test_convert()
    test_less_1()
    test_more_99()
    test_in_1_and_99()


def test_convert():
    assert convert('1/4') == 25
    assert convert('1/3') == 33
    assert convert('1/2') == 50
    assert convert('2/3') == 67
    with pytest.raises(ZeroDivisionError):
        convert('1 / 0')
    with pytest.raises(ValueError):
        convert('c/d')

def test_less_1():
    assert gauge(0.5) == 'E'
    assert gauge(1) == 'E'

def test_more_99():
    assert gauge(99.5) == 'F'
    assert gauge(99) == 'F'

def test_in_1_and_99():
    assert gauge(50) == '50%'


if __name__ == "__main__":
    main()