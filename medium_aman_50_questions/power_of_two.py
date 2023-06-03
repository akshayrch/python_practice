# In the problem of the power of two, you will be given an integer. 
# You need to return True if the integer is a power of two; otherwise, 
# return False. Below are some examples of the input and output of this problem:

# Example: 1
# Input: 16
# Output: true

import math

def power_of_two(value):
    power = 2
    check = math.log(value,power)
    return check ** power == value

print(power_of_two(17))