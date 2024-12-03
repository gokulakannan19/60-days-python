todos = []

while True:

    user_action = input("Type add, show or exit: ").strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show" | "display":
            for item in todos:
                print(item)
        case "exit":
            break
        case _:
            print("Hey you entered an unknown command")

print("Bye")