from enum import Enum


class QualityBehaviorEnum(str, Enum):
    STANDARD_DEGRADING = "StandardDegrading"
    IMPROVING_WITH_AGE = "ImprovingWithAge"
    LEGENDARY = "Legendary"
    INCREASING_UNTIL_EVENT = "IncreasingUntilEvent"


class SellInBehaviorEnum(str, Enum):
    STANDARD_DECREASE_SELL_IN = "StandardDecreaseSellIn"
    NO_CHANGE_SELL_IN = "NoChangeSellIn"


# STANDARD_DEGRADING = "StandardDegrading"
# IMPROVING_WITH_AGE = "ImprovingWithAge"
# LEGENDARY = "Legendary"
# INCREASING_UNTIL_EVENT = "IncreasingUntilEvent"
# STANDARD_DECREASE_SELL_IN = "StandardDecreaseSellIn"
# NO_CHANGE_SELL_IN = "NoChangeSellIn"
