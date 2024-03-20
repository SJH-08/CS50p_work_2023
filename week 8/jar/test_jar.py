#Import function to test
from jar import Jar

#Test initialization
def test_init():
    cookie_cap = 4
    jar = Jar(cookie_cap)
    assert jar.capacity == cookie_cap
    assert jar.size == 0
    assert Jar().capacity == 12

#Test printing and consecutive deposits (should add)
def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

#Test deposit and consecutive deposits (should add)
def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(5)
    assert jar.size == 10

#Test withdrawing and consecutive withdraw (should add)
def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(6)
    assert jar.size == 6
