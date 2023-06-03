# Finding duplicate values from an array or any other data structure is 
# one of the popular coding interview questions that you can get in any coding interview. 
# The Python programming language provides many inbuilt functions to find the duplicate values, 
# but in a coding interview, you should use an algorithm instead of an inbuilt function. 
# So if you want to learn how to find duplicate values, this article is for you. In this article, 
# I will take you through how to write a program to find duplicate values using Python.

from gettext import find


def find_duplicates(value):
    duplicates = []
    for i in range(len(value)):
        for j in range(i+1, len(value)):
            if value[i] == value[j] and value[i] not in duplicates:
                duplicates.append(value[i])
    return duplicates
        
print(find_duplicates([1,2,3,1]))