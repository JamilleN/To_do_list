#create an .txt file if there isn't one already
open("user_file.txt","a").close()
with open("user_file.txt","r") as f:
    todos = f.readlines()


def add(user_input = "add"):
    if user_input == "add":
        todo = input ("Enter a to-do: ")+"\n"
    #If user entered more than just "add", extract the 
    #task user entered
    else:
        todo = user_input[3:].strip()+"\n"
    todos.append(todo.capitalize())


def show():
    print("---------------")
    for i, item in enumerate(todos):
        print (f"{i+1} - {item}", end="")
    print("---------------")


def edit(user_input = "edit"):
    if user_input == "edit":
        num = int (input("Please enter the # to edit: "))
    else:
        num = int (user_input[5])
    
    #if the entered # is larger than # of items on list, 
    #it will add a new item instead of edit the existing one
    if num > len(todos):
        add()
    else:
        num = num - 1
        #If user only entered "edit" or the "edit + {#}", 
        #ask for what does user want to change the task to
        if (user_input == "edit" or len(user_input)<7):
            new_todo = input("Please enter the new to-do: ")+"\n"
        #If user entered more than just "add", extract the 
        #additional info
        else:
            new_todo = user_input[7:]+"\n"

    todos[num] = new_todo


def complete(user_input = "complete"):
    if user_input == "complete":
        num = int (input("Please enter the # you have completed: "))
    else:
        num = int (user_input[9])
    num = num - 1
    #added .strip() to remove the \n
    print(f"----'{num+1} - {todos.pop(num).strip()}' has been marked complete----")


def main():
    while True:
        user_input = input ("Type add, show, edit, complete or exit\n")
        user_input = user_input.strip()
        #Determine whether the user input has multiple commands, 
        #if yes aquire the action user is willing to do
        if " " in user_input:
            user_cmd = user_input[:user_input.find(" ")].lower()
        else:
            user_cmd = user_input.lower()

        match user_cmd:
            case "add":
                add(user_input)
            case "show":
                show()
            case "edit":
                edit(user_input)
                show()
            case "complete":
                complete(user_input)
                show()
            case "exit":
                break
            case default:
                print("----Invalid input, please try again.----")
        
        with open("user_file.txt","w") as f:
            f.writelines(todos)
    
    print ("Thank you for using me :)")


if __name__=="__main__":
    main()