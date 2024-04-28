from pytest import approx, raises

from calculate_stats_3 import *
from utils import test


@test
def stat_summary_raises_a_value_error_on_empty_input():
    with raises(ValueError):
        StatsReport([])


@test
def minimum_fails_on_empty_input():
    with raises(ValueError):
        minimum([])


@test
def maximum_fails_on_empty_input():
    with raises(ValueError):
        maximum([])


@test
def count_fails_on_empty_input():
    with raises(ValueError):
        count([])


@test
def average_fails_on_empty_input():
    with raises(ValueError):
        average([])


@test
def stats_report_computes_a_summary_statistic():
    stat = StatsReport([1])
    assert stat.minimum == 1
    assert stat.maximum == 1
    assert stat.count == 1
    assert stat.average == approx(1.0)


@test
def stats_report_computes_a_summary_statistic_of_multiple_items():
    stat = StatsReport([2, 1, 4, 3])
    assert stat.minimum == 1
    assert stat.maximum == 4
    assert stat.count == 4
    assert stat.average == approx(2.5)


@test
def calculate_stats_computes_the_minimum_of_one_item():
    assert minimum([1]) == 1


@test
def calculate_stats_computes_the_minimum_of_multiple_items():
    assert minimum([2, 1, 4, 3]) == 1


@test
def calculate_stats_computes_the_maximum_of_one_item():
    assert maximum([1]) == 1


@test
def calculate_stats_computes_the_maximum_of_multiple_items():
    assert maximum([2, 1, 4, 3]) == 4


@test
def calculate_stats_computes_the_count_of_one_item():
    assert count([1]) == 1


@test
def calculate_stats_computes_the_count_of_multiple_items():
    assert count([2, 1, 4, 3]) == 4


@test
def calculate_stats_computes_the_average_of_one_item():
    assert average([1]) == approx(1.0)


@test
def calculate_stats_computes_the_average_of_multiple_items():
    assert average([2, 1, 4, 3]) == approx(2.5)
