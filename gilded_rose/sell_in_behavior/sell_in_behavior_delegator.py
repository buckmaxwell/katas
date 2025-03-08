from .standard_decrease_sell_in_behavior import StandardDecreaseSellInBehavior
from .no_change_sell_in_behavior import NoChangeSellInBehavior
from .base_sell_in_behavior import BaseSellInBehavior
from ..models.item import Item
from typing import Type, Dict

from ..models.enums import SellInBehaviorEnum


class SellInBehaviorDelegator:
    BEHAVIORS: Dict[SellInBehaviorEnum, Type[BaseSellInBehavior]] = {
        SellInBehaviorEnum.STANDARD_DECREASE_SELL_IN: StandardDecreaseSellInBehavior,
        SellInBehaviorEnum.NO_CHANGE_SELL_IN: NoChangeSellInBehavior,
    }

    @staticmethod
    def update(item: Item) -> None:
        if item.sell_in_behavior is None:
            raise ValueError("Item sell_in_behavior is not defined")

        behavior_class: Type[
            BaseSellInBehavior
        ] | None = SellInBehaviorDelegator.BEHAVIORS.get(item.sell_in_behavior)
        if behavior_class:
            behavior_class.update_sell_in(item)
