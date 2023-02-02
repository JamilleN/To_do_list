open("user_file.txt","a").close()       #create an .txt file if there isn't one already
with open("user_file.txt","r") as f:
    todos = f.readlines()

def add():
    todo = input ("Enter a to-do: ")+"\n"
    todos.append(todo.capitalize())

def show():
    print("---------------")
    for i, item in enumerate(todos):
        print (f"{i+1} - {item}", end="")
    print("---------------")

def edit():
    num = int (input("Please enter the # to edit: "))
    
    if num > len(todos):      #if the entered # is larger than # of items on list, it will add a new item instead of edit the existing one
        add()
    else:
        num = num - 1
        new_todo = input("Please enter the new to-do: ")+"\n"
        todos[num] = new_todo

def complete():
    num = int (input("Please enter the # you have completed: "))
    num = num - 1
    print(f"----'{todos.pop(num).strip()}' has been marked complete----")       #added .strip() to remove the \n

def main():
    while True:
        user_input = input ("Type add, show, edit, complete or exit\n")
        user_input = user_input.strip().lower()

        match user_input:
            case "add":
                add()
            case "show":
                show()
            case "edit":
                show()
                edit()
            case "complete":
                show()
                complete()
            case "exit":
                break
            case default:
                print("----Invalid input, please try again.----")
        
        with open("user_file.txt","w") as f:
            f.writelines(todos)
    
    print ("Thank you for using me :)")


if __name__=="__main__":
    main()