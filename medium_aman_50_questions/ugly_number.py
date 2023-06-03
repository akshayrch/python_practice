# In the ugly number problem, you will be given an integer. 
# You need to check if 2, 3, and 5 are the only prime factors of the integer or not. 
# If 2, 3, and 5 are the only prime factors of the input integer, then the integer is an ugly number, 
# and your output should return true, otherwise, return false. Below is an example of the input and output of this problem:

# Input: 6
# Output: True (2×3 = 6)


class ugly_number():
    def __init__(self,value):
        self.value = value
    def prime_numbers(self):
        primes = []
        for i in range(2,self.value):
            for j in range(2, int(i ** 0.5)+1):
                if i % j != 0:
                   primes.append(i)
        return primes
    def uglynumber(value):
        if value % 2 == 0 or value % 5 == 0 or value % 3 == 0:
            return True
        return False

check = ugly_number(12)
print(check.prime_numbers())