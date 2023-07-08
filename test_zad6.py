def test_tmp(tmp_path):
    f = tmp_path / "test.txt"
    print("PLIK: ", f)
    f.write_text("Hello World!")
    fread = tmp_path / "test.txt"
    assert fread.read_text() == "Hello World!"