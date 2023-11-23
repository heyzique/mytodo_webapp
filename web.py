import streamlit as st
import functions


# function to add new item onto text file
def add_todo():
    to_do = st.session_state["new_todo"] + "\n"
    todos.append(to_do)
    functions.write_todos(todos)


# Variable to store get_todos functions (read text file)
todos = functions.get_todos()

# Layout of the streamlit page
st.title("My To-Do App")
st.subheader("The app that increases your productivity")
st.write("Try it! Create your list now!")

# List existing items & add new items that are stored
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="-", placeholder="Add new to-do...",
              on_change=add_todo, key='new_todo')
