import user_action as ua
import PySimpleGUI as psg
import local_file_interac as local
import error_code as e
import time as t

label = psg.Text("Please enter a to-do: ")
input_box = psg.InputText(tooltip="Enter your todo here", key = "todo")
list_box = psg.Listbox(values = local.get_todos(), key="todos", 
                    enable_events=True, size = [40, 10])
add_button = psg.Button("Add")
edit_button = psg.Button("Edit")
com_button = psg.Button("Complete")
clear_button = psg.Button("Clear")
exit_button = psg.Button("Exit")

window = psg.Window("My To-Do App", 
                    layout=[[label], [input_box, add_button], 
                    [list_box, edit_button], [com_button, clear_button, exit_button]], 
                    font=("Helvetica", 20))

while True:
    todos = local.get_todos()
    event, values = window.read()
    match event:
        case "Add":
            event.lower()
            todo = values["todo"]
            user_input= f"{event} {todo}"
            todos = ua.add(user_input, todos)
            window["todos"].update(values=todos)
        case "Show":
            ua.show(todos)
        case "Edit":
            event.lower()
            old_todo = values["todos"][0]
            new_todo = values["todo"][0]
            num = todos.index(old_todo) + 1
            user_input= f"{event} {num} {new_todo}"
            todos = ua.edit(user_input, todos)
            window["todos"].update(values=todos)
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case "Complete":
            event.lower()
            old_todo = values["todos"][0]
            new_todo = values["todo"][0]
            num = todos.index(old_todo) + 1
            user_input= f"{event} {num} {new_todo}"
            todos = ua.complete(user_input, todos)
            window["todos"].update(values=todos)
        case "Clear":
            todos = ua.clear(todos)
            window["todos"].update(values=todos)
        case "Exit":
            break
        case psg.WIN_CLOSED:
            break
        
    local.save_todos(todos)

print ("Thank you for using me :)")
window.close()