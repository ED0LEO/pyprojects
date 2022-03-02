def summation(i, n, a):
    summ = 0
    while i < n:
        i += 1
        summ+=a[i]
    return summ

nums = [343, 234, 2, 54, -5]
#print(summation(0, 5, nums))
