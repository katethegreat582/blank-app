import streamlit as st

st.title("Katherines Calculator")



#this does addition
st.caption("Addition")
num1 = st.number_input("num1", value=4)
num1 = int(num1)

num2 = st.number_input("num2", value=5)
num2 = int(num2)

st.button("Reset", type="primary")
if st.button("Submit"):
    st.write("Answer =",  num1+num2)


#This does subtraction
st.caption("Subtraction")
num3 = st.number_input("num3", value=6)
num3 = int(num3)

num4 =st.number_input("num4", value=7)
num4 =int(num4)

st.button("Clear", type="primary")
if st.button("Subtract"):
    st.write("Answer =",  num3-num4)


#This does multiplcation
st.caption("Multiplication")
num5 = st.number_input("num5", value=8)
num5 = int(num5)

num6 =st.number_input("num6", value=9)
num6 =int(num6)

st.button("Clean", type="primary")
if st.button("Multiply"):
    st.write("Answer =",  num5*num6)

#This does division
st.caption("Division")
num7 = st.number_input("num7", value=10)
num7 = int(num7)

num8 =st.number_input("num8", value=11)
num8 =int(num8)

st.button("Remove", type="primary")
if st.button("Divide"):
    st.write("Answer =",  num7*num8)
