from twttr import shorten
import pytest

def test_shorten_lower():
    assert shorten("hello") == "hll"

def test_shorten_upper():
    assert shorten("hEllO") == "hll"

def test_numbers():
    assert shorten("hEllo1") == "hll1"

def test_punctuation():
    assert shorten("hEllo1 BUD!") == "hll1 BD!"
