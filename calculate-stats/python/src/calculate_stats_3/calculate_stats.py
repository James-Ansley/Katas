class StatsReport:
    def __init__(self, values: list[int]):
        if len(values) == 0:
            raise ValueError("sequence is empty")
        self.values = values
        self.minimum = minimum(self.values)
        self.maximum = maximum(self.values)
        self.average = average(self.values)
        self.count = count(self.values)


def minimum(values: list[int]):
    if len(values) == 0:
        raise ValueError("sequence is empty")
    result = values[0]
    for value in values:
        if value < result:
            result = value
    return result


def maximum(values: list[int]):
    if len(values) == 0:
        raise ValueError("sequence is empty")
    result = values[0]
    for value in values:
        if value > result:
            result = value
    return result


def average(values: list[int]):
    if len(values) == 0:
        raise ValueError("sequence is empty")
    sum = 0
    for v in values:
        sum += v
    return sum / float(len(values))


def count(values: list[int]):
    if len(values) == 0:
        raise ValueError("sequence is empty")
    result = 0
    for _ in values:
        result += 1
    return result
