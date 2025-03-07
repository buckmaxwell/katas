from .sell_in_behavior.sell_in_behavior_delegator import SellInBehaviorDelegator
from .behavior.quality_behavior_delegator import QualityBehaviorDelegator


class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            SellInBehaviorDelegator.update(item)
            QualityBehaviorDelegator.update(item)
