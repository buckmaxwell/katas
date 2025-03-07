import unittest
from ..gilded_rose import GildedRose
from ..item import Item


class TestImprovingWithAgeBehavior(unittest.TestCase):
    def test_aged_brie_default_behavior(self):
        item = Item("Aged Brie", sell_in=5, quality=10)
        GildedRose([item]).update_quality()
        self.assertEqual(item.behavior, "ImprovingWithAge")
        self.assertEqual((item.sell_in, item.quality), (4, 11))

    def test_aged_brie_after_sell_date(self):
        item = Item("Aged Brie", sell_in=0, quality=10)
        GildedRose([item]).update_quality()
        self.assertEqual((item.sell_in, item.quality), (-1, 12))

    def test_aged_brie_quality_cap(self):
        item = Item("Aged Brie", sell_in=5, quality=50)
        GildedRose([item]).update_quality()
        self.assertEqual((item.sell_in, item.quality), (4, 50))
