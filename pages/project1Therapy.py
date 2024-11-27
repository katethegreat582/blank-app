import streamlit as st

st.title("Welcome to Therapy with Felica and Kate!")

st.write("We hope that you can complete the following and become filled with joy and become rejuvenated!")

with st.chat_message("user"):
    st.write("If you want to experience a moment of joy click the button and see some amazing dog pictures!!")
    st.button("Reset", type="primary")
    if st.button("Show Dog Photos:"):
        st.write()









