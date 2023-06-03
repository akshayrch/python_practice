# In the problem of counting the number of segments in a string,
# you will get a phrase or character in a string. To solve this problem,
# you need to find the total number of characters in the string, excluding the spaces.
# For example, look at the input and output of this problem shown below:

# Input: “Hey, my Instagram username is amankharwal.official” | Output: 6



def segments(value):
    a = len(value.split(' '))
    return a

value = 'Hey, my Instagram username is amankharwal.official'
print(segments(value))