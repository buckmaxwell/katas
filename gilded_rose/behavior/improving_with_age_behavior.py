class ImprovingWithAgeBehavior:
    @staticmethod
    def update_quality(item):
        if item.quality < 50:
            item.quality += 1
            if item.sell_in < 0 and item.quality < 50:
                item.quality += 1
