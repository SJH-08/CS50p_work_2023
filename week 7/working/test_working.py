#Import functions to test
from working import convert
import pytest


#Test convert hours only
def test_convert():
    assert convert("2 AM to 4 PM") == "02:00 to 16:00"
    assert convert("9 PM to 6 AM") == "21:00 to 06:00"


#Test convert with minutes
def test_with_min():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10:30 PM to 6:30 AM") == "22:30 to 06:30"


#Hour out of range
def test_wrong_hour():
#Hour > 12
    with pytest.raises(ValueError):
        convert("13 AM to 10 PM")
#Hour == 0
    with pytest.raises(ValueError):
        convert("7 AM to 0 PM")


#Minute out of range: minute > 59
def test_wrong_minute():
    with pytest.raises(ValueError):
        convert("9:60 AM to 8 PM")
    with pytest.raises(ValueError):
        convert("10 AM to 2:90 PM")


#Wrong format: no "to"
def test_wrong_format():
    with pytest.raises(ValueError):
        convert("1 AM - 10 PM")
