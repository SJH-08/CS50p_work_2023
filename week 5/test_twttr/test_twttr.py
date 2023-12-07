# Import shorten function
from twttr import shorten


# Test for numbers
def test_number():
    assert shorten("2023") == "2023"
    assert shorten("05") == "05"


# Test for punctuation
def test_punctuation():
    assert shorten("!?@&$#") == "!?@&$#"


# Test for upper and lower case
def test_upperlower():
    assert shorten("Twitter") == "Twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("twitter") == "twttr"
    assert shorten("TwiTter") == "TwTtr"

