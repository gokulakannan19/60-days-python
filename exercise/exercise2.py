persons = ["John", "Sen", "Lisa"]
user_input = input("Enter a person name").lower()
count = 1

for person in persons:
    if person.lower() == user_input:
        print(count)
    count += 1


# or we can use this

persons.index("user_input") + 1