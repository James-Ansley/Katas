from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from typing import Final

nothing: Final[object] = object()


@dataclass(frozen=True)
class StatSummary:
    min: float
    max: float
    number_of_elements: int
    average: float


def stat_summary(values: Iterable[float]) -> StatSummary:
    it = iter(values)
    first_element = next(it, nothing)
    if first_element is nothing:
        raise ValueError("Cannot compute stat summary on empty iterable")
    else:
        return _calculate_stats_with_initial(first_element, it)


def _calculate_stats_with_initial(
      first: float, rest: Iterator[float]
) -> StatSummary:
    current_min = current_max = current_total = first
    count = 1
    for element in rest:
        current_min = min(current_min, element)
        current_max = max(current_max, element)
        current_total += element
        count += 1
    return StatSummary(current_min, current_max, count, current_total / count)
