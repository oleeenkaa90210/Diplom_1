import pytest
from ingredient import Ingredient


class TestBurger():
    def test_set_buns(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun is bun

    @pytest.mark.parametrize("ingredient_name, ingredient_price", [
        ('sour cream', 200),
        ('cutlet', 100)
    ])
    def test_add_ingredient(self, ingredient_name, ingredient_price, burger):
        ingredient = Ingredient('sauce', ingredient_name, ingredient_price)
        burger.add_ingredient(ingredient)
        assert ingredient in burger.ingredients

    def test_remove_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert ingredient not in burger.ingredients

    def test_move_ingredient(self, burger, ingredient):
        ingredient2 = Ingredient('filling', 'dinosaur', 200)
        burger.add_ingredient(ingredient)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] is ingredient

    @pytest.mark.parametrize("bun_price, ingredient_price", [
        (100, 200),
        (200, 300)
    ])
    def test_get_price(self, bun_price, ingredient_price, bun_mock, ingredient_mock, burger):
        bun_mock.get_price.return_value = bun_price
        ingredient_mock.get_price.return_value = ingredient_price
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_mock)
        expected_price = bun_price * 2 + ingredient_price
        assert burger.get_price() == expected_price

    def test_get_receipt(self, burger, bun, ingredient):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        receipt = burger.get_receipt()
        assert 'black bun' in receipt
        assert 'hot sauce' in receipt
        assert 'Price: 300' in receipt
