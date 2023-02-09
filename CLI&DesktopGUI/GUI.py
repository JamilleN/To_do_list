import user_action as ua
import PySimpleGUI as psg
import local_file_interac as local
import error_code as e
import time as t

psg.theme("DarkGreen2")

clock = psg.Text("", key = "clock")
label = psg.Text("Please enter a to-do: ")
input_box = psg.InputText(tooltip="Enter your todo here", key = "inputBox", size = 46)
list_box = psg.Listbox(values = local.get_todos(), key="listBox", 
                    enable_events=True, size = [45, 10])
add_button = psg.Button("Add")
edit_button = psg.Button("Edit")
com_button = psg.Button("Complete")
clear_button = psg.Button("Clear")
exit_button = psg.Button("Exit")

window = psg.Window("My To-Do App", 
                    layout=[[clock],
                    [label], 
                    [input_box, add_button], 
                    [list_box, edit_button], 
                    [com_button, clear_button, exit_button]], 
                    font=("Helvetica", 20))

while True:
    todos = local.get_todos()
    now = t.strftime("%b %d, %Y (%a) - %H:%M:%S")
    event, values = window.read(timeout= 100)
    window["clock"].update(value = now)
    if event == psg.WIN_CLOSED:
        break
    else:
        match event:
            case "Add":
                event.lower()
                todo = values["inputBox"]
                if todo == "":
                    psg.popup("Please enter your todo item", font=("Helvetica", 20))
                else:
                    user_input= f"{event} {todo}"
                    todos = ua.add(user_input, todos)
                    window["listBox"].update(values=todos)
                    window["inputBox"].update(value="")
            case "Edit":
                try:
                    event.lower()
                    old_todo = values["listBox"][0]
                    new_todo = values["inputBox"]
                    print(values)
                    num = todos.index(old_todo) + 1
                    user_input= f"{event} {num} {new_todo}"
                    todos = ua.edit(user_input, todos)
                    window["listBox"].update(values=todos)
                except IndexError:
                    psg.popup("Please select an item first", font=("Helvetica", 20))
            case "listBox":
                window["inputBox"].update(value=values["listBox"][0].strip())
            case "Complete":
                try:
                    event.lower()
                    toComplete_todo = values["listBox"][0]
                    num = todos.index(toComplete_todo) + 1
                    user_input= f"{event} {num}"
                    todos = ua.complete(user_input, todos)
                    window["listBox"].update(values=todos)
                    window["inputBox"].update(value="")
                except IndexError:
                    psg.popup("Please select an item first", font=("Helvetica", 20))
            case "Clear":
                todos = ua.clear(todos)
                window["listBox"].update(values=todos)
                window["inputBox"].update(value="")
                psg.popup("Your todo list has been cleared. :)", font=("Helvetica", 20))
            case "Exit":
                psg.popup("Thank you for using me, have a good day! :)", font=("Helvetica", 20))
                break
    
    local.save_todos(todos)

print ("Thank you for using me :)")
window.close()