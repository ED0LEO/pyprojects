#this function will cause runtime error
def countup(n):
    if n >= 0:
        print('Blastoff!')
    else:
        print(n)
        countup(n-1)

n = input("Please, enter the number to count:")
if int(n) < 0:
    countup(int (n))
