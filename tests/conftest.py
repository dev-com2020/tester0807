import pytest

pytest_plugins = ["src.fizzbuzz.testing.fixtures"]

def pytest_runtest_setup(item):
    print("setting up", item)

@pytest.fixture()
def random_number_generator():
    import random
    def __random_provider():
        return random.choice(range(1, 10))
    yield __random_provider

@pytest.fixture(scope="function", autouse=True)
def enterexit():
    print("entering test")
    yield
    print("exiting test")

# def test_fizzbuzz(random_number_generator):