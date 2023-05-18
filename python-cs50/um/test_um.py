from um import count
import pytest

def main():
    test_one()
    test_two()
    test_three()

def test_one():
    assert count('Um um yummy') == 2
    assert count('Um, thanks for the album') == 1

def test_two():
    assert count('um') == 1
    assert count('? um...') == 1

def test_three():
    assert count('yummy') == 0

if __name__ == "__main__":
    main()