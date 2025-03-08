from pydantic import BaseModel, model_validator
from .enums import QualityBehaviorEnum, SellInBehaviorEnum
from typing import Optional


class Item(BaseModel):
    name: str
    sell_in: int
    quality: int
    behavior: Optional[QualityBehaviorEnum] = None
    sell_in_behavior: Optional[SellInBehaviorEnum] = None

    @model_validator(mode="after")
    def set_defaults(self) -> "Item":
        """Assigns default behaviors if none are provided."""
        if self.behavior is None:
            if self.name == "Aged Brie":
                self.behavior = QualityBehaviorEnum.IMPROVING_WITH_AGE
            elif self.name == "Sulfuras, Hand of Ragnaros":
                self.behavior = QualityBehaviorEnum.LEGENDARY
            elif self.name == "Backstage passes to a TAFKAL80ETC concert":
                self.behavior = QualityBehaviorEnum.INCREASING_UNTIL_EVENT
            else:
                self.behavior = QualityBehaviorEnum.STANDARD_DEGRADING

        if self.sell_in_behavior is None:
            if self.behavior == QualityBehaviorEnum.LEGENDARY:
                self.sell_in_behavior = SellInBehaviorEnum.NO_CHANGE_SELL_IN
            else:
                self.sell_in_behavior = SellInBehaviorEnum.STANDARD_DECREASE_SELL_IN

        return self
