def MiniumCostMetric(SemiRing):
    def __init__(self, field):
        self.field = field

    def or_operator(self, left, right):
        return min(left, right)

    def and_operator(self, left, right):
        return left + right
