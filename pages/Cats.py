import streamlit as st
# import pyjokes
import requests

def get_random_pokimon_image(images):
    first_image=random.randint(1,images)
    second_image=random.randint(1,images)
    pictures=(first_image+second_image)


st.image(get_random_pokimon_image(images))

images = st.slider("What image will you get?", min_value=2, max_value=20)

pictures = get_random_pokimon_image(images)

st.write("Image:", pictures)

st.button("Reroll")

response = requests.get("https://pokeapi.co/api/v2/pokemon/12/")
st.image(response.json()["sprites"]["front_default"])


# st.write(pyjokes.get_joke())