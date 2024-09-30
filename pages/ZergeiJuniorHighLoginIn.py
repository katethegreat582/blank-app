import streamlit as st

st.title("Welcome to Zergei Junior High!")

"""
We are so excited to have you joining us this year! Before you can be officially enrolled, 
we need to collect some information from you:
* Your full name
* Your age
* Your date of birth
* A photo for your official ID
* Which sports you have played so far
* Your favorite color
* Have you been on your official school visit yet?
"""

# EXAMPLE INPUT
full_name = st.text_input("What is your full name?")
age = st.text_input("How old are you?")
date_of_birth = st.text_input("What is your date of birth?")
img_file_buffer = st.camera_input("Please take a picture to verify your ID")

iimg_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as a PIL Image:
    img = Image.open(img_file_buffer)

    # To convert PIL Image to numpy array:
    img_array = np.array(img)

    # Check the type of img_array:
    # Should output: <class 'numpy.ndarray'>
    st.write(type(img_array))

    # Check the shape of img_array:
    # Should output shape: (height, width, channels)
    st.write(img_array.shape)


List_of_sports = st.text_input("Sports you have played")
Been_to_the_club = st.checkbox("I have visited")



# EXAMPLE OUTPUT
st.subheader("Student info")
st.write("Full name:", full_name)
st.write("Age:",age)
st.write("Date of birth:", date_of_birth)
st.write("Student ID:",img_file_buffer)
st.write("Sports played:",List_of_sports)
if Been_to_the_club:
    st.write("Applicant:Visited the club!")






