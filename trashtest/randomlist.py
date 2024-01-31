# create a list that has random numbers from 1 to 9
#the list should contain five members
# print the content of the list

import random
import math

evenlist = [i*2 for i in range(10)]

for i in evenlist:
	print("{} : {}".format(evenlist.index(i), i))