from pytest import raises, approx

from calculate_stats import stat_summary
from utils import test


@test
def stat_summary_raises_a_value_error_on_empty_input():
    msg = "Cannot compute stat summary on empty iterable"
    with raises(ValueError, match=msg):
        stat_summary([])


@test
def stat_summary_provides_a_summary_of_a_single_element_list():
    summary = stat_summary([1])
    assert summary.number_of_elements == 1
    assert summary.max == 1
    assert summary.min == 1
    assert summary.average == approx(1.0)


@test
def stat_summary_provides_a_summary_of_multiple_elements():
    summary = stat_summary([1, 2, 3])
    assert summary.number_of_elements == 3
    assert summary.min == 1
    assert summary.max == 3
    assert summary.average == approx(2.0)


@test
def stat_summary_iterates_once():
    data = iter([-1, -2, -3, -5, -7])
    summary = stat_summary(data)
    assert summary.number_of_elements == 5
    assert summary.min == -7
    assert summary.max == -1
    assert summary.average == approx(-3.6)
