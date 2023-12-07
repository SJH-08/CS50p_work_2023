# Import convert and gauge fct
# Import pytest for errors
from fuel import convert, gauge
import pytest


# Test for convert
def test_convert():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("1/5") == 20


# Test for gauge display
def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(60) == "60%"


# Test for division 0
def test_division_0():
    with pytest.raises(ZeroDivisionError):
        convert("5/0")
        convert("0/0")


# Test for X and Y not integers
# Test for X > Y
def test_Value():
    with pytest.raises(ValueError):
        convert("dog/cat")
        convert("three/four")
        convert("9/3")
        convert("1.5/4")
