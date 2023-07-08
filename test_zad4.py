import pytest


@pytest.fixture(scope="class")
def misiek_zdzisiek(request):
    import datetime
    request.cls.now = datetime.datetime.now()
    print("WEJŚCIE DO KLASY")
    yield
    print("\nWYJŚCIE Z KLASY")

@pytest.fixture
def greeting():
    print("\nWITAJ!\n")
    yield
    print("\nŻEGNAJ!\n")


@pytest.mark.usefixtures("misiek_zdzisiek")
class TestClass:
    def test_asercja_1(self):
        print("\nDATA ROZPOCZĘCIA TESTU: ", self.now)
        assert 1 == 1

    @pytest.mark.usefixtures("greeting")
    def test_asercja_2(self):
        assert 2 == 2