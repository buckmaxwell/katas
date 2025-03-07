class Item:
    def __init__(self, name, sell_in, quality, behavior=None, sell_in_behavior=None):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

        if behavior is None:
            if name == "Aged Brie":
                self.behavior = "ImprovingWithAge"
            elif name == "Sulfuras, Hand of Ragnaros":
                self.behavior = "Legendary"
            elif name == "Backstage passes to a TAFKAL80ETC concert":
                self.behavior = "IncreasingUntilEvent"
            else:
                self.behavior = "StandardDegrading"
        else:
            self.behavior = behavior

        if sell_in_behavior is None:
            if self.behavior == "Legendary":
                self.sell_in_behavior = "NoChangeSellIn"
            else:
                self.sell_in_behavior = "StandardDecreaseSellIn"
        else:
            self.sell_in_behavior = sell_in_behavior

    def __repr__(self):
        return f"{self.name}, {self.sell_in}, {self.quality}"
