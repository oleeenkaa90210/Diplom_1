import pytest
from ingredient import Ingredient
from tests.data import ingredient_cutlet, ingredient_cutlet_price, ingredient_sour_cream, ingredient_sour_cream_price, \
    ingredient_type, black_bun_price, white_bun_price, black_bun, ingredient_hot_sauce


class TestBurger:
    def test_set_buns(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun is bun

    @pytest.mark.parametrize("ingredient_name, ingredient_price", [
        (ingredient_sour_cream, ingredient_sour_cream_price),
        (ingredient_cutlet, ingredient_cutlet_price)
    ])
    def test_add_ingredient(self, ingredient_name, ingredient_price, burger):
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        burger.add_ingredient(ingredient)
        assert ingredient in burger.ingredients

    def test_remove_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert ingredient not in burger.ingredients

    def test_move_ingredient(self, burger, ingredient):
        ingredient2 = Ingredient(ingredient_type, ingredient_sour_cream, ingredient_sour_cream_price)
        burger.add_ingredient(ingredient)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] is ingredient

    @pytest.mark.parametrize("bun_price, ingredient_price", [
        (black_bun_price, ingredient_sour_cream_price),
        (white_bun_price, ingredient_cutlet_price)
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
        assert black_bun in receipt
        assert ingredient_hot_sauce in receipt
        assert 'Price: 300' in receipt
