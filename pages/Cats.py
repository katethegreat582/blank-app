import streamlit as st
# import pyjokes
import requests

num = st.slider("", 1. 150, 25)

response = requests.get("https://pokeapi.co/api/v2/pokemon/12/")
st.image(response.json()["sprites"]["front_default"])


# st.write(pyjokes.get_joke())