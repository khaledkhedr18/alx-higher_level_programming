height = input("How tall is the tree: ")
height = int(height)

spaces = height - 1
hashes = 1
root = height - 1

while height != 0:

	for i in range(spaces):
		print(' ', end="")
	spaces -= 1

	for i in range(hashes):
		print("#", end="")

	hashes += 2
	height -= 1
	print()

for i in range(root):
	print(' ', end="")

print("#")