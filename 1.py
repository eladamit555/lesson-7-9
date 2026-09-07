import random

def sum_seed(seed = None):
    sum_10 = 0
    random.seed(seed)
    for i in range(1, 11):
        random.randint(1, 100)
        sum_10 += random.randint(1, 100)
    return sum_10
max_sum = 0
max_seed = 0
for j in range(1, 43):
    sum_current = sum_seed(j)
    if sum_current > max_sum:
        max_sum = sum_current
        max_seed = j
    print(j, sum_current)
print()
print(max_seed, max_sum)

