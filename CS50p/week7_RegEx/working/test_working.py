from working import convert
import pytest

def test_hours_mins():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 9:30 AM") == "09:00 to 09:30"
    assert convert("2:01 PM to 3:08 PM") == "14:01 to 15:08"

def test_mix():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 9:30 AM") == "09:00 to 09:30"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:11 AM to 10 AM") == "09:11 to 10:00"
    assert convert("2:01 PM to 3:08 AM") == "14:01 to 03:08"
    assert convert("2:01 PM to 3:08 PM") == "14:01 to 15:08"

# can only do one test per with pytest
def test_errors():
    with pytest.raises(ValueError):
        convert("9:00AM to 5:00PM")
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("9AM to 5PM")
    with pytest.raises(ValueError):
        convert("8:60 PM to 9:99 AM")

