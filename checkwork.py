#Part 1
# Get estimate of the square root
def my_sqrt(a):
    x  = a;
    y = 0;
    while True:
        y = (x + a/x) / 2.0
        if y  ==  x:
            break
        x = y
    return y

print(my_sqrt(100));


#Part 2
import math;

def my_sqrt(a):
    epsilon = 0.0000001;
    x = a;
    while True:
        y = (x + a/x) / 2.0
        if abs(y-x)< epsilon:
            break;
        x = y;
    return y;

def test_sqrt():
    a = 1;
    while a<26:
        diff = my_sqrt(a) - math.sqrt(a);
        print('a =', a,'| my_sqrt(a) =',my_sqrt(a),'| math.sqrt(a) =', math.sqrt(a),'| diff =', abs(diff));
        a = a + 1;
