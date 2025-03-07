from .standard_decrease_sell_in_behavior import StandardDecreaseSellInBehavior
from .no_change_sell_in_behavior import NoChangeSellInBehavior


class SellInBehaviorDelegator:
    BEHAVIORS = {
        "StandardDecreaseSellIn": StandardDecreaseSellInBehavior,
        "NoChangeSellIn": NoChangeSellInBehavior,
    }

    @staticmethod
    def update(item):
        behavior_class = SellInBehaviorDelegator.BEHAVIORS.get(item.sell_in_behavior)
        if behavior_class:
            behavior_class.update_sell_in(item)
