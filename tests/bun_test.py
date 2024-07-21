import pytest
from bun import Bun


class TestBun():
    def test_get_name(self, bun):
        assert bun.get_name() == 'black bun'

    def test_get_price(self, bun):
        assert bun.get_price() == 100
