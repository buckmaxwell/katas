import unittest
from ..gilded_rose import GildedRose
from ..item import Item


class TestLegendaryBehavior(unittest.TestCase):
    def test_sulfuras_static_behavior(self):
        item = Item("Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)
        GildedRose([item]).update_quality()
        self.assertEqual(item.behavior, "Legendary")
        self.assertEqual((item.sell_in, item.quality), (0, 80))

    def test_new_legendary_item(self):
        item = Item("Ancient Artifact", sell_in=10, quality=80, behavior="Legendary")
        GildedRose([item]).update_quality()
        self.assertEqual((item.sell_in, item.quality), (10, 80))
