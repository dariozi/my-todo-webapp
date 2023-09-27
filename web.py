import streamlit as st
import functions

todos_list=functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"].title()
    todos_list.append(todo + "\n")
    functions.write_todos(todos_list)
    st.session_state["new_todo"] = ""



st.title("My Todo App")
st.subheader("This is my first app")
st.write("This is st.write")


for index, todo in enumerate(todos_list):
    checkbox= st.checkbox(todo, key=todo)
    if checkbox == True:
        todos_list.pop(index)
        functions.write_todos(todos_list)
        del st.session_state[todo]
        st.rerun()



st.text_input(label="", placeholder="Enter a todo", on_change=add_todo,
              key="new_todo")
