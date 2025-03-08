import unittest
from ..gilded_rose import GildedRose
from ..models.item import Item
from ..models.enums import QualityBehaviorEnum


class TestImprovingWithAgeBehavior(unittest.TestCase):
    def test_aged_brie_default_behavior(self) -> None:
        item: Item = Item(name="Aged Brie", sell_in=5, quality=10)
        gilded_rose: GildedRose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.behavior, QualityBehaviorEnum.IMPROVING_WITH_AGE)
        self.assertEqual((item.sell_in, item.quality), (4, 11))

    def test_aged_brie_after_sell_date(self) -> None:
        item: Item = Item(name="Aged Brie", sell_in=0, quality=10)
        gilded_rose: GildedRose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual((item.sell_in, item.quality), (-1, 12))

    def test_aged_brie_quality_cap(self) -> None:
        item: Item = Item(name="Aged Brie", sell_in=5, quality=50)
        gilded_rose: GildedRose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual((item.sell_in, item.quality), (4, 50))
