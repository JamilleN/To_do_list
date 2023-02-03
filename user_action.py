import local_file_interac as local
import error_code as e

def add(user_input, todos):
    if (user_input == "add" or len(user_input) == 4):
        todo = input ("Enter a to-do: ")+"\n"
    #If user entered more than just "add", extract the 
    #task user entered
    else:
        todo = user_input[3:].strip()+"\n"
    todos.append(todo.capitalize())
    show(todos)
    return todos


def show(todos):
    print("---------------")
    for i, item in enumerate(todos):
        print (f"{i+1} - {item}", end="")
    print("---------------")


def edit(user_input, todos):
    if user_input == "edit":
        num = input("P lease enter the # to edit: ")
    else:
        num = user_input[5]

    try:
        num = int(num)
        #if the entered # is larger than # of items on list, 
        #it will add a new item instead of edit the existing one
        if num > len(todos):
            add("add "+user_input[7:], todos)
        elif num > 0:
            num = num - 1
            #If user only entered "edit" or the "edit + {#}", 
            #ask for what does user want to change the task to
            if (user_input == "edit" or len(user_input) == 6):
                new_todo = input("Please enter the new to-do: ")+"\n"
            #If user entered more than just "add", extract the 
            #additional info
            else:
                new_todo = user_input[7:]+"\n"
            todos[num] = new_todo
        else:
            e.error_code.error_msg()
    except ValueError:
        e.error_msg(2)
    
    show(todos)
    return todos


def complete(user_input, todos):
    if user_input == "complete":
        num = input("Please enter the # you have completed: ")
    else:
        num = user_input[9]
    
    try:
        num = int(num)
        if (num > 0 and num <= len(todos)):
            num = num - 1
            #added .strip() to remove the \n
            print(f"----'{num+1} - {todos.pop(num).strip()}' has been marked complete----")
        else:
            e.error_msg()
    except ValueError:
        e.error_msg(2)

    show(todos)
    return todos


def clear(todos):
    todos.clear()
    print ("Your todo list has been cleared. :)")
    show (todos)
    return todos