import streamlit as st
from modules import functions


todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is a todo app to gain knowledge")
st.write("It will boost your performance")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add a new Todo...")