import pytest
from binary_search import binary_search


@pytest.mark.parametrize(
    "item_list, item, expected_index",
    [
        ([i for i in range(10)], 5, 5),
        ([i for i in range(10)], 11, None),
    ],
)
def test_binary_search_find_element(item_list, item, expected_index):
    item_index = binary_search(item_list, item)

    assert item_index == expected_index
