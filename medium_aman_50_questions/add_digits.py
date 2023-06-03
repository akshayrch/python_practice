# # In the problem of adding digits, you will be given an integer of more than one digit.
# # You need to add all the digits of the integer till you get a single-digit value as the sum.
# # Below is an example of the input and output of this problem:

# # Input: 38
# # Output: 2 (3+8 = 11, 1+1 = 2)


# class add_digits():

#     def __init__(self,value):
#         self.value = value

#     def convert_list(self):
#         return list(str(self.value))

#     def add_digits(self):
#         sum = 0
#         for i in range(len())


# check = add_digits(58)
# print(check.add_digits())

value = 25

check = value % 10 + value // 10
print(check)
