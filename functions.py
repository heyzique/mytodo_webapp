# Constant variable are in all caps
# Text file acts as a database to store existing items / new items
FILEPATH = "todo.txt"


# Custom Function
def get_todos(filepath=FILEPATH):
    # doc-string is to help other developer looking at your code
    """
    Read a text file and return the list
    to do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


# non-default parameter has to come before default param
def write_todos(todos_arg, filepath=FILEPATH):
    """
    Write the to-do items list in the text file.
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
