todos = []

print("Hello there")

while True:
    user_action = input("Type add, show, edit or exit: ").strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            for item in todos:
                print(item)
        case "edit":
            num = int(input("Enter a number of todo to edit: "))
            num = num - 1
            new_todo = input("Enter a new todo: ")
            todos[num] = new_todo
        case "exit":
            break

print("Bye")