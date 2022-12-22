import pytest
import random

from sorting import selection_sorting


@pytest.mark.parametrize(
    "input_array", [([]), ([3, 2, 1]), (random.sample(range(10, 30), 5))]
)
def test_selection_sorting(input_array):
    sorted_array = selection_sorting(input_array)

    input_array.sort()
    assert sorted_array == input_array
