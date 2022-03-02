# function for counting down for positive numbers
def countdown(n):
     if n <= 0:
          print('Blastoff!')
     else:
          print(n)
          countdown(n-1)

# function for counting down for negative numbers
def countup(n):
    if n >= 0:
        print('Blastoff!')
    else:
        print(n)
        countup(n+1)

n = input("Please, enter the number to count:")
if int(n) < 0:
    countup(int (n))
else:                               #if input number was zero it will go in "else"
    countdown(int (n))
