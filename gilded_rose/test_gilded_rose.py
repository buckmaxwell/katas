import unittest

from gilded_rose import GildedRose
from item import Item

import unittest

# --- Standard Items ---
class TestStandardDegradingBehavior(unittest.TestCase):
    def test_regular_item_before_sell_date(self):
        item = Item("Regular Item", sell_in=10, quality=20)
        GildedRose([item]).update_quality()
        self.assertEqual((item.sell_in, item.quality), (9, 19))

    def test_regular_item_after_sell_date(self):
        item = Item("Regular Item", sell_in=0, quality=20)
        GildedRose([item]).update_quality()
        self.assertEqual((item.sell_in, item.quality), (-1, 18))

    def test_regular_item_at_zero_quality(self):
        item = Item("Regular Item", sell_in=5, quality=0)
        GildedRose([item]).update_quality()
        self.assertEqual((item.sell_in, item.quality), (4, 0))


# --- Aged Brie Items ---
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


# --- Legendary Items ---
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


# --- Event-Based Items (Backstage Passes) ---
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


# --- Switched or Custom Behaviors ---
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


# --- Boundary and Edge Cases ---
class TestBoundaryConditions(unittest.TestCase):
    def test_quality_never_negative(self):
        item = Item("Regular Item", sell_in=1, quality=0)
        GildedRose([item]).update_quality()
        self.assertEqual((item.sell_in, item.quality), (0, 0))

    def test_quality_never_exceeds_fifty(self):
        item = Item("Aged Brie", sell_in=1, quality=49)
        GildedRose([item]).update_quality()
        self.assertEqual((item.sell_in, item.quality), (0, 50))


if __name__ == "__main__":
    unittest.main()
