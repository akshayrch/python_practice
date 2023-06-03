

def min_value(value):
    minimum_index = 0
    current_index = 1

    while current_index < len(value):
        if value[current_index] < value[minimum_index]:
            minimum_index = current_index
        current_index += 1
    return minimum_index


print(min_value(value=[5, 7, 4, 9, 3, 6]))
