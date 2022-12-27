import pytest
import random

from sorting import methods


@pytest.mark.parametrize(
    "input_array", [([]), ([3, 2, 1]), (random.sample(range(10, 30), 5))]
)
@pytest.mark.parametrize(
    "sorting_method", [('selection'), ('quicksort')]
)
def test_sorting_methods(input_array, sorting_method):
    method = getattr(methods, sorting_method)
    sorted_array = method(input_array)

    input_array.sort()
    assert sorted_array == input_array