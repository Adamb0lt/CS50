from plates import is_valid

def test_accepted():
    assert is_valid("AAA222") == True
    assert is_valid("AAA220") == True
    assert is_valid("BAA322") == True
    assert is_valid("AAD232") == True
    assert is_valid("AAABBB") == True
    assert is_valid("AA") == True


def test_length():
    assert is_valid("HITHERE50") == False
    assert is_valid("C3") == False
    assert is_valid("HELLO5") == True
    assert is_valid("20") == False

def test_num_placement():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AAA022") == False

def test_punctuation():
    assert is_valid("CS50.") == False






