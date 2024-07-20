import unittest
from unittest.mock import Mock
from parameterized import parameterized
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger


class TestBurger(unittest.TestCase):

    def setUp(self):
        self.bun = Bun('white bun', 200)
        self.ingredient = Ingredient('sauce', 'hot sauce', 100)
        self.burger = Burger()
        self.bun_mock = Mock()
        self.bun_mock.get_price.return_value = 200
        self.ingredient_mock = Mock()
        self.ingredient_mock.get_price.return_value = 100

    def test_set_buns(self):
        self.burger.set_buns(self.bun)
        assert self.burger.bun is self.bun

    @parameterized.expand([
        ('sour cream"', 200),
        ('cutlet', 100)
    ])
    def test_add_ingredient(self, ingredient_name, ingredient_price):
        ingredient = Ingredient('sauce', ingredient_name, ingredient_price)
        self.burger.add_ingredient(ingredient)
        self.assertIn(ingredient, self.burger.ingredients)

    def test_remove_ingredient(self):
        self.burger.add_ingredient(self.ingredient)
        self.burger.remove_ingredient(0)
        assert self.ingredient not in self.burger.ingredients

    def test_move_ingredient(self):
        ingredient2 = Ingredient('filling', 'dinosaur', 200)
        self.burger.add_ingredient(self.ingredient)
        self.burger.add_ingredient(ingredient2)
        self.burger.move_ingredient(0, 1)
        assert self.burger.ingredients[1] is self.ingredient

    @parameterized.expand([
        (100, 200),
        (200, 300)
    ])
    def test_get_price(self, bun_price, ingredient_price):
        self.bun_mock.get_price.return_value = bun_price
        self.ingredient_mock.get_price.return_value = ingredient_price
        self.burger.set_buns(self.bun_mock)
        self.burger.add_ingredient(self.ingredient_mock)
        expected_price = bun_price * 2 + ingredient_price
        assert abs(self.burger.get_price() - expected_price) < 0.01

    def test_get_receipt(self):
        self.burger.set_buns(self.bun)
        self.burger.add_ingredient(self.ingredient)
        receipt = self.burger.get_receipt()
        assert 'white bun' in receipt
        assert 'hot sauce' in receipt
        assert 'Price: 500' in receipt
