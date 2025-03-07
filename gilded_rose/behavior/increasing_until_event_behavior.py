class IncreasingUntilEventBehavior:
    @staticmethod
    def update_quality(item):
        if item.sell_in < 0:
            item.quality = 0
        else:
            if item.quality < 50:
                item.quality += 1
                if item.sell_in < 10 and item.quality < 50:
                    item.quality += 1
                if item.sell_in < 5 and item.quality < 50:
                    item.quality += 1
