import user_action as ua
import local_file_interac as local
import error_code as e


def main():
    todos = local.get_todos()

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
                todos = ua.add(user_input, todos)
            case "show":
                ua.show(todos)
            case "edit":
                todos = ua.edit(user_input, todos)
            case "complete":
                todos = ua.complete(user_input, todos)
            case "clear":
                todos = ua.clear(todos)
            case "exit":
                break
            case default:
                e.error_msg()
        
    local.save_todos(todos)    
    print ("Thank you for using me :)")


if __name__=="__main__":
    main()