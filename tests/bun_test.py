from tests.data import black_bun, black_bun_price


class TestBun:
    def test_get_name(self, bun):
        assert bun.get_name() == black_bun

    def test_get_price(self, bun):
        assert bun.get_price() == black_bun_price
