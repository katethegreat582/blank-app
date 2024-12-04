import streamlit as st

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
    st.link_button("show dog Photo 1:", image_urls[0])
    st.link_button("show dog Photo 2:", image_urls[1])
    st.link_button("show dog Photo 3:", image_urls[-1])




with st.expander("Click here to see options for animals up for adoption."):
     st.image("https://static.streamlit.io/examples/dog.jpg")
     
     
st.write("Below are quotes that can encourage and energize people.")
Bible_Quotes, John_Piper, Tim_Keller = st.tabs(["Bible", "John Piper", "Tim Keller"])

with Bible_Quotes:
    st.write("Isaiah 41:10 Fear not, for I am with you; be not dismayed, for I am your God; I will strengthen you, I will help you,I will uphold you with my righteous right hand.")
    st.write("Philippians 4:6-7 Do not be anxious about anything, but in everything by prayer and supplication with thanksgiving let your requests be made known to God. And the peace of God, which surpasses all understanding, will guard your hearts and your minds in Christ Jesus.")

with John_Piper:
    st.write("Desire that your life count for something great! Long for your life to have eternal significance. Want this! Don’t coast through life without a passion.")
    st.write("But whatever you do, find the God-centered, Christ-exalting, Bible-saturated passion of your life, and find your way to say it and live for it and die for it. And you will make a difference that lasts. You will not waste your life.")

with Tim_Keller:
     st.write("The gospel says you are simultaneously more sinful and flawed than you ever dared believe, yet more loved and accepted than you ever dared hope.")




st.write("Below are soothing sounds that help release anxiety and stress")

st.video("https://www.youtube.com/watch?v=cbOo6lpUdlY",autoplay=True)


