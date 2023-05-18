from bank import value

def main():

    test_hello()
    test_starts_h()
    test_starts_no_h()

def test_hello():
    assert value('Hello, are you ok') == 0
    assert value('Hello') == 0

def test_starts_h():
    assert value('How are you') == 20
    assert value('Hi') == 20

def test_starts_no_h():
    assert value('Wats up') == 100
    assert value('Are you ok') == 100


if __name__ == "__main__":
    main()