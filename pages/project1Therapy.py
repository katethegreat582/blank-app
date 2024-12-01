import streamlit as st
import random

st.title("Welcome to Therapy with Felica and Kate!")

st.write("We hope that you can complete the following and become filled with joy and become rejuvenated!")


image_urls = [

     ('https://hips.hearstapps.com/hmg-prod/images/little-cute-maltipoo-puppy-royalty-free-image-1652926025.jpg'),
     ('https://upload.wikimedia.org/wikipedia/commons/4/47/American_Eskimo_Dog.jpg'),
     ('https://upload.wikimedia.org/wikipedia/commons/b/b2/Dog-1123016_960_720.jpg')
  
]

with st.chat_message("user"):
    st.write("If you want to experience a moment of joy click the button and see some amazing dog pictures!!")
    st.button("Reset", type="primary")
    rand_image=random.randint(0,len(image_urls)-1)
    st.write(rand_image)
    st.link_button("show dog Photos:", image_urls[rand_image])












