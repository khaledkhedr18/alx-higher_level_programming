oneto10 = range(0,11)

def dbl_num(num):
	return num * 2

new_list = list(map(dbl_num, oneto10))

print(new_list)

lambda_list = list(map(lambda x: x *3, oneto10))

print(lambda_list)

alist = list(map(lambda x, y: x + y, [1,2,3], [1,2,3]))
print(alist)

odd_num = list(filter(lambda x: x % 2, oneto10))
even_num = list(filter(lambda x: x % 2 == 0, oneto10))

print(odd_num)
print(even_num)