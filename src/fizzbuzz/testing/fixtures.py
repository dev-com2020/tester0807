import pytest

@pytest.fixture(scope="function", autouse=True)
def announce(request):
    print("WYKONYWANIE TESTÓW", request.function)