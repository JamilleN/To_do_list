def get_todos():
    #create an .txt file if there isn't one already
    open("user_file.txt","a").close()
    with open("user_file.txt","r") as f:
        todos = f.readlines()
    return todos


def add(user_input = "add", todos = get_todos()):
    if user_input == "add":
        todo = input ("Enter a to-do: ")+"\n"
    #If user entered more than just "add", extract the 
    #task user entered
    else:
        todo = user_input[3:].strip()+"\n"
    todos.append(todo.capitalize())
    show(todos)
    return todos


def show(todos = get_todos()):
    print("---------------")
    for i, item in enumerate(todos):
        print (f"{i+1} - {item}", end="")
    print("---------------")


def edit(user_input = "edit", todos=get_todos()):
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
            if (user_input == "edit" or len(user_input) < 7):
                new_todo = input("Please enter the new to-do: ")+"\n"
            #If user entered more than just "add", extract the 
            #additional info
            else:
                new_todo = user_input[7:]+"\n"
            todos[num] = new_todo
        else:
            error_msg()
    except ValueError:
        error_msg(2)
    
    show(todos)
    return todos


def complete(user_input = "complete", todos = get_todos()):
    if user_input == "complete":
        num = input("Please enter the # you have completed: ")
    else:
        num = user_input[9]
    
    try:
        num = int(num)
        if (num > 0 and num < len(todos)):
            num = num - 1
            #added .strip() to remove the \n
            print(f"----'{num+1} - {todos.pop(num).strip()}' has been marked complete----")
        else:
            error_msg()
    except ValueError:
        error_msg(2)

    show(todos)
    return todos


def clear(todos = get_todos()):
    todos.clear()
    print ("Your todo list has been cleared. :)")
    show (todos)
    return todos


def error_msg(error_code = 1):
    match error_code:
        case 1:
            print("\n****Number is OUT OF RANGE, please try again.****\n")
        case 2:
            print("\n****Please enter a NUMBER, try again.****\n")


def main():
    todos = get_todos()

    while True:
        user_input = input ("Type add, show, edit, complete, clear or exit\n")
        user_input = user_input.strip()
        #Determine whether the user input has multiple commands, 
        #if yes aquire the action user is willing to do
        if " " in user_input:
            user_cmd = user_input[:user_input.find(" ")].lower()
        else:
            user_cmd = user_input.lower()

        match user_cmd:
            case "add":
                todos = add(user_input, todos)
            case "show":
                show(todos)
            case "edit":
                todos = edit(user_input, todos)
            case "complete":
                todos = complete(user_input, todos)
            case "clear":
                todos = clear(todos)
            case "exit":
                break
            case default:
                error_msg()
        
        with open("user_file.txt","w") as f:
            f.writelines(todos)
    
    print ("Thank you for using me :)")


if __name__=="__main__":
    main()