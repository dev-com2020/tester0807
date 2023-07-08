import pytest

@pytest.mark.first
def test_one():
    assert 1 == 1

def test_two():
    assert 2 == 2