from unittest.mock import patch, MagicMock
import pytest
from bun import Bun
from ingredient import Ingredient
from tests.data import ingredient_hot_sauce, ingredient_sour_cream, ingredient_hot_sauce_price, \
    ingredient_sour_cream_price, black_bun, black_bun_price, white_bun, white_bun_price, red_bun, red_bun_price


class TestDatabase:

    @pytest.mark.parametrize("name, price", [
        (black_bun, black_bun_price),
        (white_bun, white_bun_price),
        (red_bun, red_bun_price)
    ])
    def test_available_buns(self, name, price, database):
        buns = database.available_buns()
        bun_names = [bun.name for bun in buns]
        bun_prices = [bun.price for bun in buns]
        assert name in bun_names
        assert price in bun_prices

    @pytest.mark.parametrize("name, price", [
        (ingredient_hot_sauce, ingredient_hot_sauce_price),
        (ingredient_sour_cream, ingredient_sour_cream_price)
    ])
    def test_available_ingredients(self, name, price, database):
        ingredients = database.available_ingredients()
        ingredient_names = [ingredient.name for ingredient in ingredients]
        ingredient_prices = [ingredient.price for ingredient in ingredients]
        assert name in ingredient_names
        assert price in ingredient_prices

    @patch('database.Database.available_buns')
    def test_mock_available_buns(self, available_buns_mock, database):
        mock_buns = [MagicMock(spec=Bun) for _ in range(3)]
        available_buns_mock.return_value = mock_buns
        buns = database.available_buns()
        assert buns == mock_buns
        available_buns_mock.assert_called_once()

    @patch('database.Database.available_ingredients')
    def test_mock_available_ingredients(self, mock_available_ingredients, database):
        mock_ingredients = [MagicMock(spec=Ingredient) for _ in range(6)]
        mock_available_ingredients.return_value = mock_ingredients
        ingredients = database.available_ingredients()
        assert ingredients == mock_ingredients
        mock_available_ingredients.assert_called_once()
