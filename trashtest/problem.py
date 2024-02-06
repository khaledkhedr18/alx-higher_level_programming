#find the multiples of 9 from a random 100 value list with values between 1 and 1000
#1- import random module

import random

# 2- create an empty list

random_list = []

# 3- fill the list with 100 values from 1 to 1000

for i in range(0, 100):
	random_list.append(random.randint(1, 1001))

filtered_list = sorted(list(filter(lambda x: x % 9 == 0, random_list)))

print(filtered_list)