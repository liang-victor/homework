import pytest
from best_time_to_buy_and_sell_stock import max_profit


def test_example_1():
    prices = [7, 1, 5, 3, 6, 4]
    expected = 5

    assert max_profit(prices) == expected


def test_expect_zero_when_there_is_no_possible_gain():
    prices = [7, 6, 4, 3, 1]
    expected = 0

    assert max_profit(prices) == expected


def test_max_profit_occurs_before_lowest_price():
    prices = [3, 10, 1, 2, 3]
    expected = 7

    assert max_profit(prices) == expected


def test_zero_value_for_price():
    prices = [2, 1, 2, 1, 0, 1, 2]
    expected = 2
    assert max_profit(prices) == expected
