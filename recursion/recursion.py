def soma(arr: list) -> int:
    if arr == []:
        return 0

    return arr[0] + soma(arr[1:])


def counter(arr: list) -> int:
    if arr == []:
        return 0

    return 1 + counter(arr[1:])


def max_value(arr: list) -> int:
    if arr == []:
        return 0

    if arr[0] > max_value(arr[1:]):
        return arr[0]

    return max_value(arr[1:])
