import streamlit as st

st.title("Katherines Calculator")


num1 = st.number_input("num1", value=4)
num1 = int(num1)

num2 = st.number_input("num2", value=5)
num2 = int(num2)



if st.button("Add"):
    st.write("Answer =",  num1+num2)


if st.button("Subtract"):
    st.write("Answer =",  num1-num2)


if st.button("Multiply"):
    st.write("Answer =",  num1*num2)


if st.button("Divide"):
    st.write("Answer =",  num1/num2)
