import unittest
from ..gilded_rose import GildedRose
from ..models.item import Item


class TestBoundaryConditions(unittest.TestCase):
    def test_quality_never_negative(self) -> None:
        item: Item = Item(name="Regular Item", sell_in=1, quality=0)
        gilded_rose: GildedRose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual((item.sell_in, item.quality), (0, 0))

    def test_quality_never_exceeds_fifty(self) -> None:
        item: Item = Item(name="Aged Brie", sell_in=1, quality=49)
        gilded_rose: GildedRose = GildedRose([item])
        gilded_rose.update_quality()
        self.assertEqual((item.sell_in, item.quality), (0, 50))
