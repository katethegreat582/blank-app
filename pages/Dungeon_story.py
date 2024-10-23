import streamlit as st
st.title("My Super Crazy Adventure at Uncle Gru's!")



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
st.write("As soon as I walked through the historic door, anceint viking helmets, razer sharp axes, and dust covered paintings stuck right out at me")
st.write("Trembling with both fear and cold I understood that this would be the most and miserbarble and terrifying experience of my life!!")
st.write("Uncle Gru showed me to a bedroom in which the bed was made out of unexploded bomb and and the furniture look as if they were concoted inside a junkyard using as many explosives as possible")
st.write("The creepest thing to me is uncle gru's 'dog' which should be counted as a threat to children because he attacks all the time and looks as if he never had a bath.")
st.write("Uncle Gru's only redeeming quality is that he spends quality time with me and has some super-amazing fantastic and really insane employies")
st.write("As soon as I saw there small yellow-colored bodies covered in denim overals and almost bald heads I knew we were going to get along really well.")
st.write("After they tried to posion me and light me alive they decided I was ok and then they showed me all of the treasures my Uncle had")
st.write("In his weirly shaped house, Uncle Gru has 8 rooms dedicated to treasures.")
st.write("Here is a list of all of the treasures Uncle Gru has in his house.")
room_number =1
for room in rooms:
    treasures = ", ".join(room["treasures"])
    st.write (f"Room number {room_number} had a bunch of treasures: {treasures}")
    room_number = room_number + 1


st.write("I said there were eight rooms dedicated to treasures and that is correct. Uncle Gru once stole the moon or so he saids and the eight room marks how yes the moon is extremely important to him however his family is much more important to him. ")
st.write("After I had done some more exploring, during which I had almost died from the minons, the assistans, I found numerous more explosives and weird equipment.")
st.write("I ment a man named Dr. Nefaro, who is Uncle Gru's personal inventor. According to the Dr. there was a time inwhich Gru was the greatest villian in the world. However, Uncle Gru changed and is now working with the anti villian league to stop dangous villians.")
st.write("Dr. N informed me one villian used Gru's own minions and transformed them into super creep disjumbled monsters. Dr. N said after Uncle Gru had defeated the wacko villian he, the docter, had done several more experiments and had found how the special formual that turned them into monsters could also transform the minions into animals or things you here in books.")
st.write("Dr. N said unfortnatualy he hadn't figrued out a way to unchange the minions. He lead me down a dark hallway and opened seven doors where he showed me some of the monsters.")

room_number =1
for room in rooms:
    monsters = ", ".join(room ["monsters"])
    st.write (f"Room number {room_number} had this monster: {monsters}")
    room_number = room_number + 1
