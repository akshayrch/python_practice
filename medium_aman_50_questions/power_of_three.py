import math

class power_of_three():
    def __init__(self,value):
        self.value = value
    def power(self):
        power = int(math.log(self.value,3))
        return power ** 3 == self.value

check = power_of_three(27)
print(check.power())