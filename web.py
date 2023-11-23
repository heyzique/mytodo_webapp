import streamlit as st

st.title("My To-Do App")
st.subheader("The app that increases your productivity")
st.write("Try it! Create your list now!")

st.text_input(label="-", placeholder="Add new to-do...", key='new_todo')