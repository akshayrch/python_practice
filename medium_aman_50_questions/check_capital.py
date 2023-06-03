# In the detect capital problem, you will be given a word as input, and you need to check if:

# All the letters are uppercase: return True;
# All the letters are lowercase: return True;
# Only the first letter is uppercase: return True;
# Some letters are uppercase, and some are lowercase: return False;
# The first letter is lowercase with an uppercase letter in the word: return False;

# AKSHAY akshay Akshay these are all true
# aKSHAY AKshAY these are all false


def detect_capital(word):
    if word.isupper():
        return True
    elif word[0].isupper():
        return True
    elif word.islower():
        return True
    else:
        return False


value = input("Enter a word")
print(detect_capital(value))
