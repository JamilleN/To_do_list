f=open("user_file.txt","r")
todos = f.readlines()
f.close()

while True:
    user_input = input ("Type add, show, edit, complete or exit\n")
    user_input = user_input.strip().lower()

    match user_input:
        case "add":
            todo = input ("Enter a to-do: ")+"\n"
            todos.append(todo.capitalize())
        case "show":
            print("---------------")
            for i, item in enumerate(todos):
                print (f"{i+1} - {item}", end="")
            print("---------------")
        case "edit":
            num = int (input("Please enter the # to edit: "))
            num = num - 1
            new_todo = input("Please enter the new to-do: ")+"\n"
            todos[num] = new_todo
        case "complete":
            num = int (input("Please enter the # you have completed: "))
            num = num - 1
            print(f"----{todos.pop(num)} has been marked complete----")
        case "exit":
            break
        case default:
            print("----Invalid input, please try again.----")
    
    f=open("user_file.txt","w")
    f.writelines(todos)
    f.close()

print ("Thank you for using me :)")