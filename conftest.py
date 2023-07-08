import pytest

@pytest.fixture()
def random_number_generator():
    import random
    def __random_provider():
        return random.choice(range(1, 10))
    yield __random_provider

