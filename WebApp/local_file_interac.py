#This file has functions to read/write the local .txt file

def get_todos():
    """Read a .txt file and return the list of to-do items
    and create an .txt file if there isn't one already"""
    open("user_file.txt","a").close()
    with open("user_file.txt","r") as f:
        todos = f.readlines()
    return todos


def save_todos(todos:list):
    """save the input list into the .txt file
    """
    with open("user_file.txt","w") as f:
        f.writelines(todos)