names = ["sen", "ben", "john"]
names.sort()

for index, name in enumerate(names):
    print(f"{index+1}.{name.capitalize()}")