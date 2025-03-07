import unittest
from ..gilded_rose import GildedRose
from ..item import Item


class TestBoundaryConditions(unittest.TestCase):
    def test_quality_never_negative(self):
        item = Item("Regular Item", sell_in=1, quality=0)
        GildedRose([item]).update_quality()
        self.assertEqual((item.sell_in, item.quality), (0, 0))

    def test_quality_never_exceeds_fifty(self):
        item = Item("Aged Brie", sell_in=1, quality=49)
        GildedRose([item]).update_quality()
        self.assertEqual((item.sell_in, item.quality), (0, 50))
