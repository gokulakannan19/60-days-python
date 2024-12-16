def get_todos(filepath="files/todos.txt"):
    """" Read the text file and return the todo items"""
    with open(filepath) as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="files/todos.txt"):
    """ Write the todo items list to the text file"""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)

