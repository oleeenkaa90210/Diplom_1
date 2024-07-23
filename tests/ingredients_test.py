from tests.data import ingredient_hot_sauce_price, ingredient_type, ingredient_hot_sauce


class TestIngredient:
    def test_get_price(self, ingredient):
        assert ingredient.get_price() == ingredient_hot_sauce_price

    def test_get_name(self, ingredient):
        assert ingredient.get_name() == ingredient_hot_sauce

    def test_get_type(self, ingredient):
        assert ingredient.get_type() == ingredient_type


