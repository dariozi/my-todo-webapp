FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """Open and read the file in the filepath and assigned it to a variable"""
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos


def write_todos(todo_arg, filepath=FILEPATH):
    """Open and write the file in the filepath"""
    with open(filepath, "w") as file:
        file.writelines(todo_arg)

