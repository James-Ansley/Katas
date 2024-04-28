from pytest import raises, approx

from calculate_stats_1 import CalcStats
from utils import test


@test
def calculate_stats_fails_on_empty_input():
    calc_stats = CalcStats([])
    with raises(ValueError):
        calc_stats.minimum()
    with raises(ValueError):
        calc_stats.maximum()
    with raises(ValueError):
        calc_stats.count()
    with raises(ValueError):
        calc_stats.average()


@test
def calculate_stats_computes_the_minimum_of_lists():
    assert CalcStats([1]).minimum() == 1
    assert CalcStats([1, -1]).minimum() == -1
    assert CalcStats([41, 42, 43]).minimum() == 41
    assert CalcStats([3, 1, 2]).minimum() == 1


@test
def calculate_stats_computes_the_maximum_of_lists():
    assert CalcStats([1]).maximum() == 1
    assert CalcStats([1, -1]).maximum() == 1
    assert CalcStats([41, 42, 43]).maximum() == 43
    assert CalcStats([3, 1, 2]).maximum() == 3


@test
def calculate_stats_computes_the_count_of_lists():
    assert CalcStats([1]).count() == 1
    assert CalcStats([1, -1]).count() == 2
    assert CalcStats([41, 42, 43]).count() == 3
    assert CalcStats([3, 1, 2]).count() == 3


@test
def calculate_stats_computes_the_average_of_lists():
    assert CalcStats([1]).average() == approx(1.0)
    assert CalcStats([1, -1]).average() == approx(0.0)
    assert CalcStats([40, 42, 44]).average() == approx(42.0)
    assert CalcStats([3, 0, 2]).average() == approx(1.6666667)
