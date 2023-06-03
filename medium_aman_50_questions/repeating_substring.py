# In the Repeated Substring Pattern problem, you will be given a string. 
# To solve this problem, you need to check if the given string can be formed by repeating a substring of the string. 
# For example, look at the input and output of this problem shown below:

# Input: “abab” | Output: True


class repeating_substring():
    def __init__(self,string):
        self.string = string
    def generate_substring(self):
        substring = []
        length = len(self.string)
        for i in range(length):
            for j in range(i+1,length+1):
                substring.append(self.string[i:j])
        return substring
    def check_repeating(self):
        for i in self.generate_substring():
            if i*int((len(self.string)/len(i))) == self.string:
                return True
        return False
check = repeating_substring('ababab')
print(check.generate_substring())
print(check.check_repeating())