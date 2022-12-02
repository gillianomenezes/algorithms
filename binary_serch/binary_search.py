from math import floor


def binary_search(item_list, item):
    start = 0
    end = len(item_list) - 1
    while start <= end:
        medium = floor((start + end) / 2)
        if item_list[medium] == item:
            return medium
        elif item < item_list[medium]:
            end = medium - 1
        else:
            start = medium + 1

    return None
