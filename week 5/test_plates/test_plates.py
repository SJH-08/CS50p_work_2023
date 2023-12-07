# Import is_valid fct
from plates import is_valid


# Test for 1st nb is not 0
def test_0():
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True


# Test for
# AAA222 ok
# AAA22A no
def test_number():
    assert is_valid("CS50PH") == False
    assert is_valid("CS53") == True


# Test for length 2 <= x <= 6 chars
def test_length():
    assert is_valid("SOMEWHERE") == False
    assert is_valid("TRUE23") == True


# Test for start with at least 2 letters
def test_letter():
    assert is_valid("247") == False
    assert is_valid("XMAS23") == True


# Test for no special characters or spaces
def test_special():
    assert is_valid("PI.34") == False
    assert is_valid("AMS23") == True
