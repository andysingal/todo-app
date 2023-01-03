FILEPATH = "file/todos.txt"
def get_todos(filepath = FILEPATH):
    """
    Read a text file and return the list of to-do items

    :param filepath:
    :return:
    """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

def write_todos(todos_args,filepath=FILEPATH):
    """
    Write the to-do items list in the text files
    :param todos_args:
    :param filepath:
    :return:
    """
    with open(filepath, 'w') as file:
       file.writelines(todos_args)

print(__name__)
if __name__ == "__main__":
    print("Hello")
    print(get_todos())