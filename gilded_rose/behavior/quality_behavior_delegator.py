from ..models.enums import QualityBehaviorEnum
from .standard_degrading_behavior import StandardDegradingBehavior
from .improving_with_age_behavior import ImprovingWithAgeBehavior
from .legendary_behavior import LegendaryBehavior
from .increasing_until_event_behavior import IncreasingUntilEventBehavior


class QualityBehaviorDelegator:
    BEHAVIORS = {
        QualityBehaviorEnum.STANDARD_DEGRADING: StandardDegradingBehavior,
        QualityBehaviorEnum.IMPROVING_WITH_AGE: ImprovingWithAgeBehavior,
        QualityBehaviorEnum.LEGENDARY: LegendaryBehavior,
        QualityBehaviorEnum.INCREASING_UNTIL_EVENT: IncreasingUntilEventBehavior,
    }

    @staticmethod
    def update(item):
        behavior_class = QualityBehaviorDelegator.BEHAVIORS.get(item.behavior)
        if behavior_class:
            behavior_class.update_quality(item)
