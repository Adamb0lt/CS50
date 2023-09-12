from seasons import translate
import pytest
from datetime import date

def test_dates():
    #have to give date() function based output because of how my code is set up
    #main takes no parameters or values so I cannot import main
    assert translate("1999-01-01") == date(1999, 1, 1)

