import math

def my_sqrt(a):                     #the function to calculate the square root
    x = 3
    while True:                     #original code from the section 7.5
        y = (x + a/x) / 2.0
        if abs(y-x) < 0.0000001:    #calculate until precision is less than 0.0000001
            break
        x = y
    return (y)

def test_sqrt():
    a = 1                           #initialize a with 1 for cycle to start with this value
    while a <= 25:                  #test function on 25 values
        print("a = " + str(a) + " | my_sqrt(a) = " + str(my_sqrt(a)) + " | math.sqrt(a) = " + str(math.sqrt(a)) + " | diff = " + str(abs(math.sqrt(a)-my_sqrt(a))))
        a = a + 1                   #go to next value of a

test_sqrt()                         #run test function
