import pytest
from faker import Faker


@pytest.fixture(scope="session")
def faker():
    return Faker()
