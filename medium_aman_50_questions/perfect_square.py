#binary search problem

def perfect_square(value):
    l = 1
    r = value
    while l < r:
        mid = (l+r)//2
        if mid * mid == value:
            return True
        elif mid * mid < value:
            l = mid + 1
        elif mid * mid > value:
            r = mid
    return False

check = perfect_square(25)
print(check)