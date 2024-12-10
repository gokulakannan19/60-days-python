while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()


    if "add" in user_action:

        todo = user_action[4:] + "\n"

        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo)
        print(todos)

        with open("files/todos.txt", "w") as file:
            file.writelines(todos)

    elif "show" in user_action:

        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}-{item}")

    elif "edit" in user_action:
        num = int(user_action[5:])
        num = num - 1

        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

        new_todo = input("Enter a new todo: ") + "\n"
        todos[num] = new_todo

        with open("files/todos.txt", "w") as file:
            file.writelines(todos)

    elif "complete" in user_action:
        num = int(user_action[9:])

        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

        todos_to_remove = todos.pop(num - 1).strip("\n")

        print(f"{todos_to_remove} was removed from the list")


        with open("files/todos.txt", "w") as file:
            file.writelines(todos)

    elif "exit" in user_action:
        break

    else:
        print("Command is not valid")

print("Bye")