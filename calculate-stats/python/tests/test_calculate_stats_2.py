from pytest import approx, raises

from calculate_stats_2 import *
from utils import test


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
def calculate_stats_computes_the_minimum_of_lists():
    assert minimum([1]) == 1
    assert minimum([1, -1]) == -1
    assert minimum([41, 42, 43]) == 41
    assert minimum([3, 1, 2]) == 1


@test
def calculate_stats_computes_the_maximum_of_lists():
    assert maximum([1]) == 1
    assert maximum([1, -1]) == 1
    assert maximum([41, 42, 43]) == 43
    assert maximum([3, 1, 2]) == 3


@test
def calculate_stats_computes_the_count_of_lists():
    assert count([1]) == 1
    assert count([1, -1]) == 2
    assert count([41, 42, 43]) == 3
    assert count([3, 1, 2]) == 3


@test
def calculate_stats_computes_the_average_of_lists():
    assert average([1]) == approx(1.0)
    assert average([1, -1]) == approx(0.0)
    assert average([40, 42, 44]) == approx(42.0)
    assert average([3, 0, 2]) == approx(1.6666667)
