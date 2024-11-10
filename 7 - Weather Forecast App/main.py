import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select a number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature","Sky"))

st.subheader(f"{option} for the next {days} days in {place}")
print("Aqui empieza")
if place:
    #Get temperature/sky data
    try:
        filtered_data = get_data(place,days)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"] for dict in filtered_data]
            temperatures = [temperature / 10 for temperature in temperatures]
            dates = [dict["dt_txt"] for dict in filtered_data]
            #Create temperature Plot
            figure = px.line(x=dates, y=temperatures,labels={"x":"Dates","y":"Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images =  {"Clear": "images/clear.png","Clouds":"images/cloud.png", "Rain":"images/rain.png", "Snow":"images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            images_paths = [images[condition] for condition in sky_conditions]
            st.image(images_paths, width= 115)
    except KeyError:
        st.info("Place doesnt exist in recods")