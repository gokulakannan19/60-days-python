todos = []

while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            for index, item in enumerate(todos):
                print(f"{index+1}-{item}")
        case "edit":
            num = int(input("Enter a number of todo to edit: "))
            num = num - 1
            new_todo = input("Enter a new todo: ")
            todos[num] = new_todo
        case "complete":
            num = int(input("Enter the number of the todo to complete: "))
            todos.pop(num-1)
        case "exit":
            break

print("Bye")