import requests
import streamlit as st
import credentiales


url = f"https://api.nasa.gov/planetary/apod?api_key={credentiales.api_key}"



request = requests.get(url)

#Get a dictionary with data
content = request.json()


st.title(content["title"])
st.image(content["url"])
st.write(content["explanation"])
