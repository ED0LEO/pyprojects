import math

def power(base, power_arg):
    if (power_arg == 0 and base == 0):              #different break cases
        return (1)
    elif (base == 0):
        return (1)
    elif (power_arg == 0):
        return (1)
    elif (power_arg < 0):
        return (0)
    return base * power(base, power_arg - 1)        #recursion until power_arg will be zero

def sq_root(number):
    num = 0
    while (math.floor(num * num) != number ):       #this loop will work until the number multiplied by itself won't be close enough to argument
        if (num > number):
            return (None)
        num += 0.0001                               #incrementing value by small portions for better precision
    return (num)

def hypotenuse(a, b):
    c = sq_root(power(a, 2) + power(b, 2))          #calculation hypothenuse
    return (c)

print(hypotenuse(3, 4))
print(hypotenuse(34, 5))
print(hypotenuse(56, 45))
print(hypotenuse(23, 10))
