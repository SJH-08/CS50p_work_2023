# Import Value function
from bank import value


#Test for int values
# Test for $0
def test_value0():
    assert value("Hello ") == 0
    assert value("Hello, Newman") == 0


# Test for $20
def test_value20():
    assert value("How you doing? ") == 20
    assert value("Hey") == 20


# Test for $100
def test_value100():
    assert value("What's up?") == 100
    assert value("What's your name?") == 100
