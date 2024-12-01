import streamlit as st
import random

st.title("Welcome to Therapy with Felica and Kate!")

st.write("We hope that you can complete the following and become filled with joy and become rejuvenated!")


image_urls = [
#    (https://example.com/dog1.jpg),
#    (https://example.com/dog2.jpg)
     ('https://hips.hearstapps.com/hmg-prod/images/little-cute-maltipoo-puppy-royalty-free-image-1652926025.jpg'),
     ('https://upload.wikimedia.org/wikipedia/commons/b/b2/Dog-1123016_960_720.jpg')
#     ("https://google.com")   
]
rand_image=random.radinit(0,len(image_urls))

with st.chat_message("user"):
    st.write("If you want to experience a moment of joy click the button and see some amazing dog pictures!!")
    st.button("Reset", type="primary")
#    if st.link_button("show dog Photos:", image_urls):
#    st.link_button("show dog Photos:", "https://www.google.com")
#    st.link_button("show dog Photos:", "https://hips.hearstapps.com/hmg-prod/images/little-cute-maltipoo-puppy-royalty-free-image-1652926025.jpg")
    st.link_button("show dog Photos:", image_urls[rand_image])

#            st.write("(%s)" % image_urls)










