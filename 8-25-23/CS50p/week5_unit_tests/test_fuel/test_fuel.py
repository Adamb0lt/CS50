from fuel import convert, gauge
import pytest



def test_convert():
    assert convert("1/2") == 50
    assert convert("1/100") == 1
    assert convert("99/100") == 99


def test_convert_error():
    with pytest.raises(ValueError):
        convert("2/1")
    with pytest.raises(ZeroDivisionError):
        convert("3/0")
        #another error is below
''' with pytest.raises(TypeError):
        convert("cat")'''

def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"