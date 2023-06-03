# Hamming distance between two integers is a measure of the difference between two strings of equal length. 
# In this problem, you will be given two integers, and you need to calculate the number of positions 
# where the corresponding bits are different. 
# For example, look at the input and output of this problem shown below:

# Input: x = 1, y = 4 | Output: 2
# In the above example, there are two integers: 1 and 4. 
# The binary representation of 1 is 0001, and the binary representation of 4 is 0100. 
# There are two positions where the corresponding bits of the integers are different. So the output is 2.

#Appraoch:
#1) Find the binary representation of the numbers
#2) Loop over the numbers in 1 and loop over the numbers in other and check for the same one
#3) Have a count variable and use an IF condition to get the count

a = 1
b = 4

xor = a ^ b
print(xor)