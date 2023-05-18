from plates import is_valid

def main():
    test_min_max()
    test_start_with_two_letter()
    test_no_punctuation()
    test_teart_with_zero()
    test_no_number_middle()

def test_min_max():
    assert is_valid('A') == False
    assert is_valid('AB') == True
    assert is_valid('ABCDEFGH') == False
    assert is_valid('ABCDEF') == True


def test_start_with_two_letter():
    assert is_valid('AB') == True
    assert is_valid('ABC') == True
    assert is_valid('1A') == False
    assert is_valid('A1') == False

def test_no_punctuation():
    assert is_valid('A.B') == False
    assert is_valid('AB 12') == False
    assert is_valid('AB ') == False

def test_teart_with_zero():
    assert is_valid('AB01') == False
    assert is_valid('AB10') == True

def test_no_number_middle():
    assert is_valid('AB12AB') == False
    assert is_valid('AB1212') == True

if __name__ == "__main__":
    main()