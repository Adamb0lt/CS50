from numb3rs import validate
import pytest

def test_validate_pos_wrong():
    assert validate("275.3.6.28") == False
    assert validate("3.275.6.28") == False
    assert validate("6.28.275.3") == False
    assert validate("3.6.28.275") == False

def test_validate_not_number():
    assert validate("cat") == False

def test_validate_neg_wrong():
    assert validate("275.-3.6.28") == False
    assert validate("-3.275.6.28") == False
    assert validate("6.28.275.-3") == False
    assert validate("3.6.-28.275") == False

def test_validate_1limit_right():
    assert validate("255.3.6.28") == True
    assert validate("3.255.6.28") == True
    assert validate("6.28.255.3") == True
    assert validate("3.6.28.255") == True

def test_validate_maxlimit_right():
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("1.2.3.4") == True

def test_octets():
    assert validate("255") == False
    assert validate("3.255") == False
    assert validate("6.28.255") == False
    assert validate("3.6.cat.255") == False




