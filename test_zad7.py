def myapp():
    print("Aplikacja uruchomiona")


def test_myapp(capsys):
    myapp()
    out, err = capsys.readouterr()
    assert out == "Aplikacja uruchomiona\n"