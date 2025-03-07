import unittest
from ..gilded_rose import GildedRose
from ..models.item import Item
from ..models.enums import QualityBehaviorEnum


class TestCustomBehaviorAssignments(unittest.TestCase):
    def test_regular_item_with_aged_brie_behavior(self) -> None:
        item: Item = Item(
            "Regular Cheese",
            sell_in=5,
            quality=10,
            behavior=QualityBehaviorEnum.IMPROVING_WITH_AGE,
        )
        gilded_rose: GildedRose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual((item.sell_in, item.quality), (4, 11))

    def test_event_item_with_legendary_behavior(self) -> None:
        item: Item = Item(
            "Exclusive Concert Pass",
            sell_in=5,
            quality=80,
            behavior=QualityBehaviorEnum.LEGENDARY,
        )
        gilded_rose: GildedRose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual((item.sell_in, item.quality), (5, 80))
