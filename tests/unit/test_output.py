from src.fizzbuzz import outfizz


def test_outfizz(capsys):
    outfizz()
    out, _ = capsys.readouterr()
    assert out == "fizz"
