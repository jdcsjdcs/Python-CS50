from seasons import validate

def main():
    test_vaidate()


def test_vaidate():
    assert validate('2001.Dec.21.') == None
    assert validate('2001.12.21') == None
    assert validate('2001-12-21') == ('2001', '12', '21')


if __name__ == "__main__":
    main()