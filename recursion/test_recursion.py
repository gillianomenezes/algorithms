import pytest
from recursion import soma, counter, max_value
from random import randint


@pytest.mark.parametrize("input_array, expected_result", [([2, 4, 6], 12), ([], 0)])
def test_soma(input_array, expected_result):
    result = soma(input_array)

    assert result == expected_result


@pytest.mark.parametrize(
    "input_array, expected_result", [([randint(0, 9) for _ in range(10)], 10), ([], 0)]
)
def test_counter(input_array, expected_result):
    result = counter(input_array)

    assert result == expected_result


@pytest.mark.parametrize(
    "input_array, expected_result", [([randint(0, 9) for _ in range(10)], 9), ([], 0)]
)
def test_max_value(input_array, expected_result):
    result = max_value(input_array)

    assert result == expected_result
