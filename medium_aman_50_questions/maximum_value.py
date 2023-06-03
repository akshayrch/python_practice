# Python has a built-in function to find the maximum value in a list. You can also define your Python function for the same task.
# But the question here is to find the index of the maximum value instead of the value itself.
# So here is how you can define a Python function to find the index of the maximum value in a Python list:


def max_value(value):
    max_value = 0

    for i in range(len(value)):
        if value[i] > max_value:
            max_value = value[i]

    return value.index(max_value)


print(max_value(value=[5, 7, 4, 9, 3, 6]))
