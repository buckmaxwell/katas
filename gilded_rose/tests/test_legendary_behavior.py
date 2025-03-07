import unittest
from ..gilded_rose import GildedRose
from ..models.item import Item
from ..models.enums import QualityBehaviorEnum


class TestLegendaryBehavior(unittest.TestCase):
    def test_sulfuras_static_behavior(self) -> None:
        item: Item = Item("Sulfuras, Hand of Ragnaros", sell_in=0, quality=80)
        gilded_rose: GildedRose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.behavior, QualityBehaviorEnum.LEGENDARY)
        self.assertEqual((item.sell_in, item.quality), (0, 80))

    def test_new_legendary_item(self) -> None:
        item: Item = Item(
            "Ancient Artifact",
            sell_in=10,
            quality=80,
            behavior=QualityBehaviorEnum.LEGENDARY,
        )
        gilded_rose: GildedRose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual((item.sell_in, item.quality), (10, 80))
