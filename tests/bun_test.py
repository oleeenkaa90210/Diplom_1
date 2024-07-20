import unittest
from praktikum.bun import Bun


class TestBun(unittest.TestCase):

    def setUp(self):
        self.bun = Bun('black bun', 100)

    def test_get_name(self):
        self.assertEqual(self.bun.get_name(), 'black bun')

    def test_get_price(self):
        self.assertEqual(self.bun.get_price(), 100)
