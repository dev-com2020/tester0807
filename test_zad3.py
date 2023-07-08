import pytest


@pytest.fixture
def greeting():
    print("\nWITAJ!\n")
    yield
    print("\nŻEGNAJ!\n")


class TestMultiple:
    def test_first_assert_1_1(self):
        assert 1 == 1

    @pytest.mark.usefixtures("greeting")
    def test_second(self):
        assert 2 == 2