import unittest
from ..gilded_rose import GildedRose
from ..models.item import Item


class TestCustomBehaviorAssignments(unittest.TestCase):
    def test_regular_item_with_aged_brie_behavior(self):
        item = Item(
            "Regular Cheese", sell_in=5, quality=10, behavior="ImprovingWithAge"
        )
        GildedRose([item]).update_quality()
        self.assertEqual((item.sell_in, item.quality), (4, 11))

    def test_event_item_with_legendary_behavior(self):
        item = Item(
            "Exclusive Concert Pass", sell_in=5, quality=80, behavior="Legendary"
        )
        GildedRose([item]).update_quality()
        self.assertEqual((item.sell_in, item.quality), (5, 80))
