import streamlit as st
import random



# HOMEWORK: Make the get_roll function work!
def get_roll(num_sides):
    first_roll=random.randint(1,num_sides)
    second_roll=random.randint(1,num_sides)
    roll=(first_roll+second_roll)
    return roll
st.write("Roll two dice and get the result")

num_sides = st.slider("How many sides should your dice have?", min_value=2, max_value=20)

roll = get_roll(num_sides)

st.write("Roll is:", roll)

st.button("Reroll")