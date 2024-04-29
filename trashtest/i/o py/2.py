import os

with open("mydata.txt", mode="w", encoding="utf-8") as myFile:
	myFile.write("Some random text\nMore random text\nand some random text")

with open("mydata.txt", mode="r", encoding="utf-8") as myFile:
	print(myFile.read())

print(myFile.closed)
print(myFile.name)
print(myFile.mode)
