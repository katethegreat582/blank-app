import streamlit as st

output = st.checkbox("Brush your teeth")
st.write(output)

todos = {
    "Brush your teeth": False,
    "Comb your hair": False,
    "Wake up": True,
}

st.write(todos)

if st.button("Add a new item"):
    ...

if "brushed_my_teeth" not in st.session_state:
    st.session_state["brushed_my_teeth"] = ["Way to Go"]

if st.button("Completed brushing teeth"):
    st.session_state["brushed_my_teeth"].append("Way to go!")

st.write(str(st.session_state))
