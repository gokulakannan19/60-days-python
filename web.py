import streamlit as st
from modules import functions


todos = functions.get_todos()


def add_todo():
    todo_local = st.session_state["new_todo"] + "\n"
    todos.append(todo_local)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is a todo app to gain knowledge")
st.write("It will boost your performance")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        # pass
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label=" ", placeholder="Add a new Todo...",
              on_change=add_todo, key="new_todo")

st.session_state