# A phrase, word, or number is a palindrome if it reads the same backward as forward.
# For validating palindrome words, you will be given words or phrases as input, 
# and you have to check if it is palindrome or not. If it’s in a palindrome sequence, 
# you need to return True, else False.

# For example, have a look at the input and output of this problem below:

# Input: “A man, a plan, a canal: Panama”
# Output: True

from re import I


def validate_palindrome(value):
    new_value = ''
    for i in value:
        if i.isalnum():
            new_value += i
    return  new_value.casefold() == new_value[::-1].casefold()
print(validate_palindrome('A man, a plan, a canal: Panama'))