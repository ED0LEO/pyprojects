def average(nums):  #the average function can be used to calculate average value of the argument elements
    sum = 0         #sum is used for sum of the argument elements
    amount = 0      #amount is used for hold number of the argument elements
    for num in nums:
        sum += num
        amount += 1
    print(sum/amount)

average([2, 2, 2])
average([1, 2, 3, 4, 5])
average([3423, 2, 0, 384, -5])
