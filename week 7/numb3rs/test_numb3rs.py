#Import function to test
from numb3rs import validate


#Valid tests
def test_validate():
    assert validate("1.2.3.4") == True
    assert validate("0.255.0.255") == True
    assert validate("0.0.0.0") == True
    assert validate("8.28.195.3") == True


#Incorrect inputs (formats)
def test_format():
    assert validate("0") == False
    assert validate("275.0") == False
    assert validate("0.0.0.") == False
    assert validate("1000.5.6.7") == False


#Incorrect inputs (test each 4 possibilities and other values)
def test_input():
    assert validate("cat") == False
    assert validate("360.275.890.456") == False
    assert validate("1.275.2.3") == False
    assert validate("2.3.890.4") == False
    assert validate("4.5.6.456") == False
