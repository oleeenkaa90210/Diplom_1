import unittest
from praktikum.ingredient import Ingredient


class TestIngredient(unittest.TestCase):

    def setUp(self):
        self.ingredient_type = 'sauce'
        self.name = 'Соус Spicy-X'
        self.price = 90.0
        self.ingredient = Ingredient(self.ingredient_type, self.name, self.price)

    def test_get_price(self):
        assert self.ingredient.get_price() == self.price

    def test_get_name(self):
        assert self.ingredient.get_name() == self.name

    def test_get_type(self):
        assert self.ingredient.get_type() == self.ingredient_type
