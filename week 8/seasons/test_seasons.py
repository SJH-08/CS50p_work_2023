from seasons import get_dob
import pytest


#Test for correct format
def test_right_format():
    assert get_dob("1995-08-08") == "Fourteen million, nine hundred seventy-eight thousand, eight hundred eighty minutes"
    assert get_dob("2023-01-30") == "Five hundred twenty-five thousand, six hundred minutes"
    assert get_dob("2024-01-01") == "Forty-one thousand, seven hundred sixty minutes"


#Test for incorrect format
def test_invalid_format():
#No -
    with pytest.raises(SystemExit):
        get_dob("2000,03,25")
#Wrong order
    with pytest.raises(SystemExit):
        get_dob("13-09-1769")

