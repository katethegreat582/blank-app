import streamlit as st

def what_type_is_it(thing):
    st.write(f"value = `{thing}`")
    st.write(f"data type = `{type(thing).__name__}`")
    st.divider()

x = st.button("Press me")

what_type_is_it(x)

x = st.checkbox("Check me")

what_type_is_it(x)

x = st.number_input("Enter something")

what_type_is_it(x)

x = st.number_input("Enter something", value=3)

what_type_is_it(x)

x = st.text_input("Enter something", value="Hi")

what_type_is_it(x)

x = st.multiselect(
    "What are your favorite colors",
    ["Green", "Yellow", "Red", "Blue"],
    ["Yellow", "Red"],
)

what_type_is_it(x)

st.write("""
Your assignment:
         
Go to https://docs.streamlit.io/develop/api-reference/widgets
         
Pick two more input widgets and add them to this page, and see what 
types of variable comes out of each one.
         
Hint: use `what_type_is_it()`
         
What would you use that input for?
""")

# PUT YOUR CODE BELOW THIS:

activated = st.toggle("activate")
what_type_is_it(activated)



choice = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions=[
        "Laugh out loud.",
        "Get the popcorn.",
        "Never stop learning.",
    ],
)
what_type_is_it(choice)

picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)