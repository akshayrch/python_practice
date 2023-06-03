# In the FizzBuzz problem, you will be given an integer, and you need to return a string array where:

# the numbers that are divisible by 3 will be replaced with the word “Fizz”;
# the numbers that are divisible by 5 will be replaced with the word “Buzz”;
# and the numbers that are divisible by both 3 and 5 will be replaced by the word “FizzBuzz”;
# Below is an example of the input and output of this problem:

# Input: 3 | Output: [“1”, “2”, “Fizz”]
# Input: 5 | Output: [“1”, “2”, “Fizz”, “4”, “Buzz”]

# Appraoch:
#     build a list from the length given [0,1,2] <> [1,2,3]
#     condition 1 is 3 and 5
#     condition 2 is 3 and condition 3 is 5
#     else return the value


def fizzbuzz(value):
    new_list = []
    for i in range(1, value+1):
        if i % 3 == 0 and i % 5 == 0:
            new_list.append('FizzBuzz')
        if i % 5 == 0:
            new_list.append('Buzz')
        if i % 3 == 0:
            new_list.append('Fizz')
        else:
            new_list.append(i)
    return new_list

check = int(input('Enter a number greater than zero'))
print(fizzbuzz(check))