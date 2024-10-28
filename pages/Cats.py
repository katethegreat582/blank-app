import streamlit as st
import pyjokes
import requests

st.write("# requests")

response = requests.get("https://pokeapi.co/api/v2/pokemon/12/")
st.image(response.json()["sprites"]["front_default"])


# st.write(pyjokes.get_joke())