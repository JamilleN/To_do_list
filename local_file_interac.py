def get_todos():
    #create an .txt file if there isn't one already
    open("user_file.txt","a").close()
    with open("user_file.txt","r") as f:
        todos = f.readlines()
    return todos


def save_todos(todos):
    with open("user_file.txt","w") as f:
        f.writelines(todos)