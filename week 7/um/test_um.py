from um import count

#Test valid input for Um alone as word
def test_um_ok():
    assert count("Um") == 1
    assert count("Um?") == 1
    assert count("Um ok let's see") == 1

#Test for um in words
def test_um_word():
    assert count("Yummy") == 0
    assert count("Album") == 0
    assert count("instrument") == 0

#Test for case sensitivity
def test_case():
    assert count("UM ") == 1
    assert count("um ...") == 1
    assert count("Um you know what?") == 1
