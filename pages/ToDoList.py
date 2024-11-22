import streamlit as st

st.title("The Ultimate Wake up To Do List!")


brush_teeth = st.checkbox("Brush teeth")
Take_a_shower = st.checkbox("Take a shower")
Make_Bed = st.checkbox("Make Bed")
Complete_SkinCare = st.checkbox("Complete skin care routine")
Dress = st.checkbox("Get dressed")


if st.button("Add a new item"):
    title = st.text_input("Extra Items to complete", "")
    


