import unittest
from ..gilded_rose import GildedRose
from ..item import Item


class TestIncreasingUntilEventBehavior(unittest.TestCase):
    def test_backstage_pass_default_behavior(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20)
        GildedRose([item]).update_quality()
        self.assertEqual(item.behavior, "IncreasingUntilEvent")
        self.assertEqual((item.sell_in, item.quality), (14, 21))

    def test_backstage_pass_close_to_event(self):
        item = Item(
            "Backstage passes", sell_in=10, quality=20, behavior="IncreasingUntilEvent"
        )
        GildedRose([item]).update_quality()
        self.assertEqual((item.sell_in, item.quality), (9, 22))

    def test_backstage_pass_very_close_to_event(self):
        item = Item(
            "Backstage passes", sell_in=5, quality=20, behavior="IncreasingUntilEvent"
        )
        GildedRose([item]).update_quality()
        self.assertEqual((item.sell_in, item.quality), (4, 23))

    def test_backstage_pass_after_event(self):
        item = Item(
            "Backstage passes", sell_in=0, quality=20, behavior="IncreasingUntilEvent"
        )
        GildedRose([item]).update_quality()
        self.assertEqual((item.sell_in, item.quality), (-1, 0))
