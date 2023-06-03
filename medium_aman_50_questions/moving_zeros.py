# In the problem of moving zeroes, you will be given an array of zero and non-zero elements in random order.
# To solve the problem of moving zeroes, you need to move all the zeroes present in the array at the end of the array.
# Besides moving the zeroes, you don’t need to change the order of other non-zero elements.
# Below is an example of the input and output of this problem:

# Input: [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]


def moving_zeroes(value):
    check_0 = 0
    for i in range(len(value)):
        if value[i] != 0:
            value[check_0], value[i] = value[i], value[check_0]
            check_0 += 1
    return value


value = [0, 1, 0, 3, 12]
print(moving_zeroes(value))
