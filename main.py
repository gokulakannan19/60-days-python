while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    match user_action:
        case "add":

            todo = input("Enter a todo: ") + "\n"

            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            todos.append(todo)
            print(todos)

            with open("files/todos.txt", "w") as file:
                file.writelines(todos)

        case "show":

            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip("\n")
                print(f"{index + 1}-{item}")

        case "edit":
            num = int(input("Enter a number of todo to edit: "))
            num = num - 1

            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            new_todo = input("Enter a new todo: ") + "\n"
            todos[num] = new_todo

            with open("files/todos.txt", "w") as file:
                file.writelines(todos)

        case "complete":
            num = int(input("Enter the number of the todo to complete: "))

            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            todos_to_remove = todos.pop(num - 1)

            print(f"{todos_to_remove} was removed from the list")


            with open("files/todos.txt", "w") as file:
                file.writelines(todos)

        case "exit":
            break

print("Bye")