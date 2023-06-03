# you will be given a number,
# and you need to check whether the number is equal to the sum of its divisors,
# excluding the number itself. For example, 6 is a perfect number because its divisors (excluding itself) are 1, 2, and 3,
# and 1 + 2 + 3 = 6. If it’s a perfect number, your output should return True, otherwise False.
# For example, look at the input and output values of this problem shown below:

# Input: 28 | Output: True
# Input: 7 | Output: False


def perfect_number(num):
    if num <= 1:
        return False
    sum = 1
    divisor = 2
    while divisor < num:
        if num % divisor == 0 and num != divisor:
            sum += divisor
        divisor += 1
    if sum == num:
        return True
    else:
        return False


value = int(input("Enter a number"))
print(perfect_number(value))
