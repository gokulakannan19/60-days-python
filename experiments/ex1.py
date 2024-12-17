import glob

myfiles = glob.glob("../files/*.txt")

# print(myfiles)
for filepath in myfiles:
    with open(filepath, "r") as file:
        print(file.readlines())

#
# a = 5
# b= 5
# sum = a + b