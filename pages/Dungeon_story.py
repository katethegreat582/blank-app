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

st.write("I went up to my rich great uncle for the weekend. It changed my life forever.  ")
st.write("As soon as I walked through the door over the cricking wooden bords, anceint viking helmets, razer sharp axes, and dust covered paintings stuck right out at me")
st.write("trembling with both fear and cold I understood that this would be the most dark, cold, and miserbarble experience of my life!!")


room_number =1
for room in rooms:
    treasures = ", ", join(room ["treasures"])
    st.write (f"Room number {room_number} had a bunch of treasures:")
    room_number = room_number + 1