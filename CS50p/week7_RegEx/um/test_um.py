from um import count
import pytest

def test_um():
    assert count("um i um") == 2
    assert count("i um i um") == 2
    assert count("umbrella i um") == 1
    assert count("um  i  um") == 2
    assert count("um") == 1
    assert count("Um") == 1


def test_punc():
    assert count("um!") == 1
    assert count("um?") == 1
    assert count("um*") == 1
    assert count("um\\") == 1

