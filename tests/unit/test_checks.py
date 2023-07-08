import pytest

from src.fizzbuzz import isfizz, isbuzz


# def test_isfizz():
#     assert isfizz(3)
#     assert not isfizz(4)
#
# def test_isbuzz():
#     assert isbuzz(5)
#     assert not isbuzz(6)

@pytest.mark.parametrize("n,res", [
    (1, False),
    (3, True),
    (4, False),
    (5, False),
    (6, True)])
def test_isfizz(n, res):
    assert isfizz(n) is res


@pytest.fixture()
def divisible_by_5(n):
    return n % 5 == 0


@pytest.mark.parametrize("n", [1, 3, 5, 6, 10])
def test_isbuzz(n, divisible_by_5):
    assert isbuzz(n) is divisible_by_5
