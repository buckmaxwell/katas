import unittest
from ..gilded_rose import GildedRose
from ..models.item import Item


class TestStandardDegradingBehavior(unittest.TestCase):
    def test_regular_item_before_sell_date(self) -> None:
        item: Item = Item("Regular Item", sell_in=10, quality=20)
        gilded_rose: GildedRose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual((item.sell_in, item.quality), (9, 19))

    def test_regular_item_after_sell_date(self) -> None:
        item: Item = Item("Regular Item", sell_in=0, quality=20)
        gilded_rose: GildedRose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual((item.sell_in, item.quality), (-1, 18))

    def test_regular_item_at_zero_quality(self) -> None:
        item: Item = Item("Regular Item", sell_in=5, quality=0)
        gilded_rose: GildedRose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual((item.sell_in, item.quality), (4, 0))
