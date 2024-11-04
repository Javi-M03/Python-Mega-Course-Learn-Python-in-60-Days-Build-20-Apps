import requests
import streamlit as st


api_key = "4G0dQ2JVfxEE1D6cejkfAkmKqdJ5fmwWDIzBJHfJ"
url = "https://api.nasa.gov/planetary/apod?api_key=4G0dQ2JVfxEE1D6cejkfAkmKqdJ5fmwWDIzBJHfJ"



request = requests.get(url)

#Get a dictionary with data
content = request.json()


st.title(content["title"])
st.image(content["url"])
st.write(content["explanation"])
