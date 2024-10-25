import streamlit as st
st.title("My Super Crazy Adventure at my sevenths cousins great uncles son Gru's!")



rooms = [
    {
        "treasures": ["gold coin", "gem"],
        "monsters": ["goblin"],
        "clues": ["map to next room"],
    },
    {
        "treasures": ["silver coin"],
        "monsters": ["troll"],
        "clues": ["look behind the rock"],
    },
    {
        "treasures": ["diamond"],
        "monsters": ["dragon"],
        "clues": ["use the key to open the door"],
    },
    {
        "treasures": ["ruby"],
        "monsters": ["giant spider"],
        "clues": ["spiders are afraid of light"],
    },
    {
        "treasures": ["emerald"],
        "monsters": ["unicorn", "giant eagle"],
        "clues": ["unicorns are afraid of the dark"],
    },
    {
        "treasures": ["sapphire"],
        "monsters": ["giant squid"],
        "clues": ["the sapphire is actually a glass lock"],
    },
    {
        "treasures": ["opal", "ruby"],
        "monsters": ["giant eagle"],
        "clues": ["the unicorn loves to play in the pool and relaxes with her favorite snack a latte"],
    },
]

st.write("I went up to my sevenths cousins twice removed great uncles son Gru's for the weekend. It changed my percpective of life forever.")
st.write("As soon as I walked through the historic front door, ancient viking helmets, razer sharp axes, and dust covered paintings stuck right out at me.")
st.write("Trembling with both fear and cold I though that this would be the most miserbarble and terrifying experience of my life!!")
st.write("Uncle Gru showed me to a bedroom in which the bed was made out of an unexploded bomb and and the furniture look as if it was concoted inside a junkyard using as many explosives as possible.")
st.write("I decided to start exploring where I was going to be for the next 24 hours. Mr. Gru has a very frightening taste for his house. However, the creepest thing to me is Mr. Gru's 'dog' which should be counted as a threat to children, attacks all the time and looks as if he never had a bath.")
st.write("Uncle Gru's only redeeming quality is that he spends quality time with me and has some super-amazing fantastic and really insane employies")
st.write("As soon as I saw there small yellow-colored bodies covered in denim overals and almost bald heads I knew we were going to get along really well.")
st.write("After they tried to posion me and light me alive they decided I was ok and then they showed me all of the treasures Mr. Gru had.")
st.write("In his weirdly shaped house, Uncle Gru has 8 rooms dedicated to treasures.")
st.write("Here is a list of all of the treasures Uncle Gru has in his house.")
room_number =1
for room in rooms:
    treasures = ", ".join(room["treasures"])
    st.write (f"Room number {room_number} had a bunch of treasures: {treasures}")
    room_number = room_number + 1


st.write("I said there were eight rooms dedicated to treasures and that is correct. Mr. Gru once stole the moon or so he saids and the eight room marks how yes the moon is extremely important to him however his family is much more important to him. ")
st.write("After I had done some more exploring, during which I had almost died from the minons, the assistans, I found numerous more explosives and weird equipment.")
st.write("I ment a man named Dr. Nefaro, who is Uncle Gru's personal inventor. According to the Dr. there was a time inwhich Gru was the greatest villian in the world. However, Uncle Gru changed and is now working with the anti villian league to stop dangous villians.")
st.write("Dr. N informed me one villian used Gru's own minions and transformed them into super creepy disjumbled monsters. Dr. N said after Mr. Gru had defeated the villian he, the docter, had done several more experiments and had found how the special formual that turned the minions into monsters could also transform the minions into animals or things you read in books.")
st.write("Dr. N said unfortnatualy he hadn't figrued out a way to unchange the minions. He lead me down a dark hallway and opened seven doors where he showed me some of the monsters.")

st.write("List of Monsters:")
room_number =1
for room in rooms:
    monsters = ", ".join(room ["monsters"])
    st.write (f"Room number {room_number} had this monster: {monsters}")
    room_number = room_number + 1

st.write("By this time, not only was my heart rate was beating a million beats per second because of the minions constantly trying to kill me, I was also extremely hungry!")
st.write("By the time I finaly found the kitchen, my stomach was rumbiling as loudly as a screaming kid trying to hit a pinata. When I walked into the kitchen I noticed some intresting decorations and observed three girls making heart-shaped sugar cookies. I intorducted myself and they responded by telling me they were my cousins and they told me their names.")
st.write("I took an instant liking to these girls. After gobbiling 12 of the delicous pink sugar cookies, I asked my new friends if they wanted to do something.")
st.write("Eidith the blond girl with a pink hat promptly responded that we could cover me in mud and stick me into an anceint Egyptian coffin. Marrgo the eldest, quickly vetoed that motion and said that she had a treasure map and that if we could solve she would make us root beer floats! I love nothing more than a foamy root beer float so I quickly agreed along with my relatives.")
st.write("Margo handed us a paper which had a map drawn on it. The paper stated there were 7 rooms with a secret in each. Each room would lead us to the next step of the hunt. Margo had already circled the first room and said all the secrets gave a clue to what we needed to bring to her.")


st.write("Long story short these are the secrets we found it each room.")
room_number =1
for room in rooms:
    clues = ", ".join(room ["clues"])
    st.write (f"Room number {room_number} had this clue: {clues}")
    room_number = room_number + 1

st.write("We solved each of the clues that lead us to the next room however on the last one we did not understand what we were to bring to Margo until I saw the coffee bar in the kitchen. I promptly made a latte and handed it to Margo. ")
st.write("Right as Margo started to get the ice cream out for the root beer float Mrs. Gru came in.")
st.write("We unfortanutaly had to pospone having root beer floats. Mrs. Gru asked us to help her with dinner and soon I found myself sitting at the table with steaming soup and freshly baked bread in front of me. After an amazing dinner, Mrs. Gru said that we could make our root beer floats. Mr. Gru then suggjested that we play charades. I was with Agnes and Mr. Gru. We won because Agnes is a natural at guessing.")
st.write("By that time it was time for bed so I headed to my bedroom. As I lay there on the bed, I relized that even though the Gru family may be unusal they prioritize important things and that matters more than all the other things in the world.")
st.write("I was woken up the next morning to a flood of minions running into my room. I played games wtih the minions and the girls all morning and by the time I had to leave I realized I really think I would want to spend my next vacation with my amazing relatives and friends!")

