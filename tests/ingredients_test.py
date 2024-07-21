class TestIngredient():
    def test_get_price(self, ingredient_spicy):
        price = 90.0
        assert ingredient_spicy.get_price() == price

    def test_get_name(self, ingredient_spicy):
        name = 'Соус Spicy-X'
        assert ingredient_spicy.get_name() == name

    def test_get_type(self, ingredient_spicy):
        ingredient_type = 'sauce'
        assert ingredient_spicy.get_type() == ingredient_type
