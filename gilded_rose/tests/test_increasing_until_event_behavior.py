import unittest
from ..gilded_rose import GildedRose
from ..models.item import Item
from ..models.enums import QualityBehaviorEnum


class TestIncreasingUntilEventBehavior(unittest.TestCase):
    def test_backstage_pass_default_behavior(self) -> None:
        item: Item = Item(
            name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20
        )
        gilded_rose: GildedRose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual(item.behavior, QualityBehaviorEnum.INCREASING_UNTIL_EVENT)
        self.assertEqual((item.sell_in, item.quality), (14, 21))

    def test_backstage_pass_close_to_event(self) -> None:
        item: Item = Item(
            name="Backstage passes",
            sell_in=10,
            quality=20,
            behavior=QualityBehaviorEnum.INCREASING_UNTIL_EVENT,
        )
        gilded_rose: GildedRose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual((item.sell_in, item.quality), (9, 22))

    def test_backstage_pass_very_close_to_event(self) -> None:
        item: Item = Item(
            name="Backstage passes",
            sell_in=5,
            quality=20,
            behavior=QualityBehaviorEnum.INCREASING_UNTIL_EVENT,
        )
        gilded_rose: GildedRose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual((item.sell_in, item.quality), (4, 23))

    def test_backstage_pass_after_event(self) -> None:
        item: Item = Item(
            name="Backstage passes",
            sell_in=0,
            quality=20,
            behavior=QualityBehaviorEnum.INCREASING_UNTIL_EVENT,
        )
        gilded_rose: GildedRose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual((item.sell_in, item.quality), (-1, 0))
