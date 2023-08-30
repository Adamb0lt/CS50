from bank import value
import pytest

def test_hello():
    assert value("hello") == 0

def test_starts_with_h():
    assert value("h") == 20
    assert value("hi there") == 20

def test_no_h():
    assert value("thanks for coming") == 100
    assert value("appreciate you") == 100

def test_number_with_h():
    assert value("1hp") == 100

def test_number_with_caps():
    assert value("Hi Adam") == 20
    assert value("HELLO there") == 0

