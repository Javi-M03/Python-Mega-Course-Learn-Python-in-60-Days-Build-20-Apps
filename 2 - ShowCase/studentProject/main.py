import streamlit as st
import pandas 

df = pandas.read_csv("data.csv")
st.set_page_config(layout='wide')

st.header("The best company")
content = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis suscipit porta velit, quis faucibus nulla euismod quis.
 Sed commodo diam non urna mollis, nec facilisis nisl aliquet. Morbi mattis vulputate posuere. Orci varius natoque penatibus
et magnis dis parturient montes, nascetur ridiculus mus. Ut risus diam,
 tempus at ex nec, euismod egestas dui. Phasellus non facilisis ipsum, sed faucibus purus. Donec maximus et metus vitae mattis.
"""

st.write(content)

st.subheader("Our Team")

col1, empty_col1, col2,empty_col2, col3, empty_col3 = st.columns([1.5,0.5,1.5,0.5,1.5,0.5])

with col1:
    for index,row in df[:4].iterrows():
        st.header(f"{row['first_name'].capitalize()} {row['last_name'].capitalize()} ")
        st.write(row["role"])
        st.image("images/" + row["image"])

with col2:
    for index,row in df[4:8].iterrows():
        st.header(f"{row['first_name'].capitalize()} {row['last_name'].capitalize()} ")
        st.write(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index,row in df[8:].iterrows():
        st.header(f"{row['first_name'].capitalize()} {row['last_name'].capitalize()} ")
        st.write(row["role"])
        st.image("images/"+row['image'])