from unittest.mock import Mock
import pytest
from bun import Bun
from burger import Burger
from database import Database
from ingredient import Ingredient
from tests.data import black_bun, black_bun_price, ingredient_type, ingredient_hot_sauce, ingredient_hot_sauce_price, \
    white_bun_price, ingredient_cutlet_price


@pytest.fixture
def bun():
    return Bun(name=black_bun, price=black_bun_price)


@pytest.fixture
def ingredient():
    return Ingredient(ingredient_type=ingredient_type, name=ingredient_hot_sauce, price=ingredient_hot_sauce_price)


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def bun_mock():
    bun_mock = Mock()
    bun_mock.get_price.return_value = white_bun_price
    return bun_mock


@pytest.fixture
def ingredient_mock():
    ingredient_mock = Mock()
    ingredient_mock.get_price.return_value = ingredient_cutlet_price
    return ingredient_mock


@pytest.fixture
def database():
    return Database()
