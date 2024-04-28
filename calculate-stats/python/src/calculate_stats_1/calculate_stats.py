import statistics


class CalcStats:
    def __init__(self, values: list[int]):
        self.values = values

    def minimum(self):
        return min(self.values)

    def maximum(self):
        return max(self.values)

    def average(self):
        return statistics.fmean(self.values)

    def count(self):
        if len(self.values) == 0:
            raise ValueError("sequence is empty")
        else:
            return len(self.values)
