from numb3rs import validate

def main():
    test_validate_a()
    test_validate_b()

def test_validate_a():
    assert validate('1') == False
    assert validate('1.2') == False
    assert validate('1.2.3') == False
    assert validate('1.2.3.4') == True
    assert validate('cat') == False

def test_validate_b():
    assert validate('256.255.255.0') == False
    assert validate('255.256.255.0') == False
    assert validate('255.255.255.255') == True
    assert validate('0.0.0.0') == True
    assert validate('0.255.10.1000') == False

if __name__ == "__main__":
    main()