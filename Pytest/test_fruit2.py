import pytest
from fruit2 import Fruit

@pytest.fixture
def fruit():
    return Fruit

