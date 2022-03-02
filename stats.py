import statistics

# generate random integer values
from random import seed
from random import randint
# seed random number generator
seed(1)
# generate some integers
n = 100
values = []
for _ in range(n):
	values.append(randint(0, 10))

print("mean = ", statistics.mean(values))
print("median = ", statistics.median(values))
