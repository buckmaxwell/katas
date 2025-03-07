from .standard_degrading_behavior import StandardDegradingBehavior
from .improving_with_age_behavior import ImprovingWithAgeBehavior
from .legendary_behavior import LegendaryBehavior
from .increasing_until_event_behavior import IncreasingUntilEventBehavior


class QualityBehaviorDelegator:
    BEHAVIORS = {
        "StandardDegrading": StandardDegradingBehavior,
        "ImprovingWithAge": ImprovingWithAgeBehavior,
        "Legendary": LegendaryBehavior,
        "IncreasingUntilEvent": IncreasingUntilEventBehavior,
    }

    @staticmethod
    def update(item):
        behavior_class = QualityBehaviorDelegator.BEHAVIORS.get(item.behavior)
        if behavior_class:
            behavior_class.update_quality(item)
