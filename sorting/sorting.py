def get_lower_element_index(array):
    lower = array[0]
    lower_index = 0
    for i in range(1, len(array)):
        if lower > array[i]:
            lower = array[i]
            lower_index = i

    return lower_index


def selection_sorting(input_array):
    if len(input_array) < 0:
        return input_array

    array = input_array.copy()
    sorted_array = []

    for _ in range(len(array)):
        lower_index = get_lower_element_index(array)
        sorted_array.append(array.pop(lower_index))

    return sorted_array
