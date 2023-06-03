# In the problem of checking duplicate values, you will be given an array of integers. 
# You need to check if any value appears more than once. 
# Below is an example of the input and output of this problem:
    
# Input: [1, 2, 3, 1]
# Output: True

from hashlib import new


def check_dups(value):
    new_list = []
    for i in range(len(value)):
        if value[i] in new_list:
            return True
            break
        else:
            new_list.append(value[i])
    return False

print(check_dups([1,2,3,4,1]))