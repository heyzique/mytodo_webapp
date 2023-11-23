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

st.text_input(label="-", placeholder="Add new to-do...",
              on_change=add_todo, key='new_todo')
