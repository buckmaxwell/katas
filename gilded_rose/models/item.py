from .enums import QualityBehaviorEnum, SellInBehaviorEnum


class Item:
    def __init__(
        self,
        name: str,
        sell_in: int,
        quality: int,
        behavior: QualityBehaviorEnum | None = None,
        sell_in_behavior: SellInBehaviorEnum | None = None,
    ) -> None:
        self.name: str = name
        self.sell_in: int = sell_in
        self.quality: int = quality

        # Assign default behavior based on item name
        if behavior is None:
            if name == "Aged Brie":
                self.behavior = QualityBehaviorEnum.IMPROVING_WITH_AGE
            elif name == "Sulfuras, Hand of Ragnaros":
                self.behavior = QualityBehaviorEnum.LEGENDARY
            elif name == "Backstage passes to a TAFKAL80ETC concert":
                self.behavior = QualityBehaviorEnum.INCREASING_UNTIL_EVENT
            else:
                self.behavior = QualityBehaviorEnum.STANDARD_DEGRADING
        else:
            self.behavior = behavior

        # Assign default sell_in behavior
        if sell_in_behavior is None:
            if self.behavior == QualityBehaviorEnum.LEGENDARY:
                self.sell_in_behavior = SellInBehaviorEnum.NO_CHANGE_SELL_IN
            else:
                self.sell_in_behavior = SellInBehaviorEnum.STANDARD_DECREASE_SELL_IN
        else:
            self.sell_in_behavior = sell_in_behavior
