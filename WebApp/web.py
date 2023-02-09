import streamlit as sl
import local_file_interac as local

def add_todo():
    todo = sl.session_state["new_todo"]+"\n"
    if not (todo.strip()==""):
        todos.append(todo)
        local.save_todos(todos)

todos = local.get_todos()

sl.title("My Todo App")

for i, todo in enumerate(todos):    
    checkbox = sl.checkbox(todo, key = todo)
    if checkbox:
        todos.pop(i)
        local.save_todos(todos)
        del sl.session_state[todo]
        sl.experimental_rerun()

sl.text_input(label="Please enter your todo below: ", 
                placeholder="Add a new todo", on_change=add_todo, key="new_todo")
