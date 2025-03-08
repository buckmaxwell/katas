from typing import Dict, Type
from ..models.enums import QualityBehaviorEnum
from ..models.item import Item
from .base_behavior import BaseBehavior
from .standard_degrading_behavior import StandardDegradingBehavior
from .improving_with_age_behavior import ImprovingWithAgeBehavior
from .legendary_behavior import LegendaryBehavior
from .increasing_until_event_behavior import IncreasingUntilEventBehavior


class QualityBehaviorDelegator:
    BEHAVIORS: Dict[QualityBehaviorEnum, Type[BaseBehavior]] = {
        QualityBehaviorEnum.STANDARD_DEGRADING: StandardDegradingBehavior,
        QualityBehaviorEnum.IMPROVING_WITH_AGE: ImprovingWithAgeBehavior,
        QualityBehaviorEnum.LEGENDARY: LegendaryBehavior,
        QualityBehaviorEnum.INCREASING_UNTIL_EVENT: IncreasingUntilEventBehavior,
    }

    @staticmethod
    def update(item: Item) -> None:
        if item.behavior is None:
            raise ValueError("Item behavior is not defined")

        behavior_class: Type[
            BaseBehavior
        ] | None = QualityBehaviorDelegator.BEHAVIORS.get(item.behavior)
        if behavior_class:
            behavior_class.update_quality(item)
