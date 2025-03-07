from .base_sell_in_behavior import BaseSellInBehavior
from ..models.item import Item


class StandardDecreaseSellInBehavior(BaseSellInBehavior):
    @staticmethod
    def update_sell_in(item: Item) -> None:
        item.sell_in -= 1
