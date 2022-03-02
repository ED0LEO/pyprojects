def is_divisible(x, y):                         #function to check is x can be divided by y without a remaining
    return x % y == 0

def is_power(a, b):
    if (a < 0 or b < 0):                        #wrong arguments value check
        return None
    if (b == 1 and a != b):                     #case of 1
        return False
    if (b == 0):                                #case of 0
        return a == 0 or a == 1
    if (a == b):                                #recursion break statement
        return True
    if (is_divisible(a, b) and is_power(a/b, b)):     #recursion to check if a/b is a power of b
            return True
    return False

print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))

#additional tests
print("a=2 b=1 ", is_power(2, 1))
print("a=1 b=2 ", is_power(1, 2))
print("a=1 b=0 ", is_power(1, 0))
print("a=5 b=0 ", is_power(5, 0))
print("a=25 b=5 ", is_power(25, 5))
print("a=10 b=5 ", is_power(10, 5))
print("a=5 b=5 ", is_power(5, 5))
print("a=10 b=-3 ", is_power(10, -3))
print("a=3 b=5 ", is_power(3, 5))
print("a=2 b=1 ", is_power(2, 1))
print("a=4 b=2 ", is_power(4, 2))
print("a=625 b=2 ", is_power(625, 2))
print("a=19683 b=3 ", is_power(19683, 3))
