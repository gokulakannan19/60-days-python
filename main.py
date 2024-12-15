def get_todos(filepath):
    with open(filepath) as file_local:
        todos_local = file.readlines()
    return todos_local


def write_todos(filepath, todos_arg):
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)


while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"
        todos = get_todos("files/todos.txt")
        todos.append(todo)
        write_todos(filepath="files/todos.txt", todos_arg=todos)

    elif user_action.startswith("show"):
        todos = get_todos("files/todos.txt")
        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}-{item}")

    elif user_action.startswith("edit"):
        try:
            num = int(user_action[5:])
            num = num - 1
            todos = get_todos("files/todos.txt")
            new_todo = input("Enter a new todo: ") + "\n"
            todos[num] = new_todo
            write_todos(filepath="files/todos.txt", todos_arg=todos)
        except ValueError:
            print("You entered invalid command")
            continue

    elif user_action.startswith("complete"):
        try:
            num = int(user_action[9:])
            todos = get_todos("files/todos.txt")
            todos_to_remove = todos.pop(num - 1).strip("\n")
            print(f"{todos_to_remove} was removed from the list")
            write_todos(filepath="files/todos.txt", todos_arg=todos)
        except ValueError:
            print("Invalid command")
            continue
        except IndexError:
            print("Item is not in the list")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is not valid")

print("Bye")