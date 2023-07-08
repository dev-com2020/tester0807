import pytest

import src.fizzbuzz
from src.fizzbuzz import outfizz, outbuzz


# def test_outfizz(capsys):
#     outfizz()
#     out, _ = capsys.readouterr()
#     assert out == "fizz"
#
# def test_outbuzz(capsys):
#     outbuzz()
#     out, _ = capsys.readouterr()
#     assert out == "buzz"

@pytest.fixture(params=["fizz", "buzz"])
def expected_output(request):
    yield getattr(src.fizzbuzz, "out{}".format(request.param)), request.param

def test_output(expected_output,capsys):
    func,expected = expected_output
    func()
    out, _ = capsys.readouterr()
    assert out == expected

# def test_output(capsys):