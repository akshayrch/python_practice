#  string is a sequence of characters enclosed in single or double-quotes. 
#  String inversion is one of the most common problems in computer science.
#  Here we need to reverse the characters of a string. 
#  So, if you want to learn how to reverse a string, this article is for you. 
#  In this article, I will walk you through a tutorial on how to reverse a string using


class reverse_str():
    def __init__(self,value):
        self.value = value
    
    def rev(self):
        return self.value[::-1]
    
check = reverse_str('akshay')
print(check.rev())