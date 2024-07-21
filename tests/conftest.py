from unittest.mock import Mock
import pytest
from bun import Bun
from burger import Burger
from database import Database
from ingredient import Ingredient


@pytest.fixture
def bun():
    bun = Bun(name='black bun', price=100)
    return bun


@pytest.fixture
def ingredient():
    ingredient = Ingredient(ingredient_type='sauce', name='hot sauce', price=100)
    return ingredient

@pytest.fixture
def ingredient_spicy():
    ingredient = Ingredient(ingredient_type='sauce', name='Соус Spicy-X', price=90)
    return ingredient

@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def bun_mock():
    bun_mock = Mock()
    bun_mock.get_price.return_value = 200
    return bun_mock


@pytest.fixture
def ingredient_mock():
    ingredient_mock = Mock()
    ingredient_mock.get_price.return_value = 100
    return ingredient_mock


@pytest.fixture
def database():
    return Database()

