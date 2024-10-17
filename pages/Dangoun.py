import streamlit as st

rooms = [
    {
        "treasures": ["gold coin", "gem"],
        "monsters": ["goblin"],
        "secrets": ["map to next room"],
    },
    {
        "treasures": ["silver coin"],
        "monsters": ["troll"],
        "secrets": ["look behind the rock"],
    },
    {
        "treasures": ["diamond"],
        "monsters": ["dragon"],
        "secrets": ["use the key to open the door"],
    },
    {
        "treasures": ["ruby"],
        "monsters": ["giant spider"],
        "secrets": ["spiders are afraid of fire"],
    },
    {
        "treasures": ["emerald"],
        "monsters": ["unicorn", "giant eagle"],
        "secrets": ["unicorns are afraid of the dark"],
    },
    {
        "treasures": ["sapphire"],
        "monsters": ["giant squid"],
        "secrets": ["squids are afraid of the light", "the sapphire is actually glass"],
    },
    {
        "treasures": ["opal", "ruby"],
        "monsters": ["giant eagle"],
        "secrets": ["the eagle is actually a hologram"],
    },
]

st.title("Welcome to the dungeon! 👹")

st.write("Print out the first room:")
room = rooms[0]
st.write(room)

st.write("Print out the 3rd room:")
room = rooms[2]
st.write(room)

st.write("Print out the last room:")
room = rooms[-1]
st.write(room)

st.write("Print out the treasures in the 2nd room:")
room_treasure = rooms[1]["treasures"]
st.write(room_treasure)

st.write("Print out the monsters in the 4th room:")
room_monster = rooms[3]["monsters"]
st.write(room_monster)

st.write("Print out the second secret in the 5th room:")
room_secret_second_part = rooms[-2]["secrets": (1)]
st.write(room_secret_second_part)



#student["Favorite color"]