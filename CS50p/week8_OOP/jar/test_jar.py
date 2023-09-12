from jar import Jar
import pytest


def test_init():
    jar = Jar()

#tests the __str__
def test_str():
    #start by calling the class and then testing it with  assertion of str class
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(2)
    assert str(jar) == "🍪🍪"
    jar.deposit(10)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.deposit(23)


def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(5)
    assert jar.size == 7
    with pytest.raises(ValueError):
        jar.withdraw(23)