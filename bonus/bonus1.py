def get_average():
    with open("../files/data.txt") as file:
        data = file.readlines()[1:]

    values = [float(value) for value in data]
    print(values)

    average_local = sum(values) / len(values)
    return average_local


average = get_average()
print(average)