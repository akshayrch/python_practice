# candidates often face algorithmic problems that require them to manipulate and reformat input data.

# One such problem involves reformatting a license key represented as a string. 
# The string consists of alphanumeric characters and hyphens and is separated into n + 1 groups by n hyphens (“-“). 
# The task is to reformat the string so that each group contains exactly k characters, except for the first group, 
# which can be shorter than k but must always contain at least one character.

# Also, all lowercase letters must be converted to uppercase, and a hyphen must be inserted between two groups. 
# Let’s take a look at an example to better understand the problem:

# Input: s =n 371534930, \CIF\NYSE\AWS_EXTRACT\FINRA_SHORT_INTEREST\set_local_variables\130_data_delivery “2-4A0r7-4k”, k = 3 | Output: “24-A0R-74K” "25A0-R7-4K"
# In the example above, the input string “2-4A0r7-4k” is reformatted so that each group contains three characters 
# (except the first group), all lowercase letters are converted to uppercase, and a hyphen is inserted between two groups.

# Captialize all the values
# Get the count of the value and get th counts of the - and split accordingly
# Split the string by '-'
# Loop over the rest of the groups
# Check the length of the individual groups
# If there is a mismatch move the last or first character to the other group based on which comes first
from hashlib import new

value = '2-4A0r7-4k'
value = value.upper().replace('-','')
k = 3
length = len(value)
  
new_list = []
value = value[::-1]
# print(value)

for i in range(0,length,k):
    new_list.append(value[i:i+k])

key = '-'.join(new_list)[::-1]
print(new_list)
print(key)