import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.database = Database()

    @parameterized.expand([
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300)
    ])
    def test_available_buns(self, name, price):
        buns = self.database.available_buns()
        bun_names = [bun.name for bun in buns]
        bun_prices = [bun.price for bun in buns]
        assert name in bun_names
        assert price in bun_prices

    @parameterized.expand([
        ("hot sauce", 100),
        ("sour cream", 200),
        ("chili sauce", 300),
        ("cutlet", 100),
        ("dinosaur", 200),
        ("sausage", 300)
    ])
    def test_available_ingredients(self, name, price):
        ingredients = self.database.available_ingredients()
        ingredient_names = [ingredient.name for ingredient in ingredients]
        ingredient_prices = [ingredient.price for ingredient in ingredients]
        assert name in ingredient_names
        assert price in ingredient_prices

    @patch('praktikum.database.Database.available_buns')
    def test_mock_available_buns(self, mock_available_buns):
        mock_buns = [MagicMock(spec=Bun) for _ in range(3)]
        mock_available_buns.return_value = mock_buns
        buns = self.database.available_buns()
        assert buns == mock_buns
        mock_available_buns.assert_called_once()

    @patch('praktikum.database.Database.available_ingredients')
    def test_mock_available_ingredients(self, mock_available_ingredients):
        mock_ingredients = [MagicMock(spec=Ingredient) for _ in range(6)]
        mock_available_ingredients.return_value = mock_ingredients
        ingredients = self.database.available_ingredients()
        assert ingredients == mock_ingredients
        mock_available_ingredients.assert_called_once()

