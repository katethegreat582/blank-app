import streamlit as st
import random



# HOMEWORK: Make the get_roll function work!



st.write("Roll two dice and get the result")

num_sides = st.slider("How many sides should your dice have?", min_value=2, max_value=20)
get_roll = random.randint[(1,7)]

roll = get_roll(num_sides)

st.write("Roll is:", roll)
