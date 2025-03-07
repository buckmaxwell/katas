from .sell_in_behavior.sell_in_behavior_delegator import SellInBehaviorDelegator
from .behavior.quality_behavior_delegator import QualityBehaviorDelegator
from .models.item import Item
from typing import List


class GildedRose:
    def __init__(self, items: List[Item] = []) -> None:
        self.items: List[Item] = items

    def update_quality(self) -> None:
        for item in self.items:
            SellInBehaviorDelegator.update(item)
            QualityBehaviorDelegator.update(item)
