from ..models.item import Item
from .base_behavior import BaseBehavior


class StandardDegradingBehavior(BaseBehavior):
    @staticmethod
    def update_quality(item: Item) -> None:
        if item.quality > 0:
            item.quality -= 1
            if item.sell_in < 0 and item.quality > 0:
                item.quality -= 1
