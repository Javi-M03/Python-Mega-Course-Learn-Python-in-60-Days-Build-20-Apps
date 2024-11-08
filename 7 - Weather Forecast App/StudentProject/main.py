import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv("happy.csv")

st.title("In Search for Happiness")
x_axis=st.selectbox("Select the data for the X-axis",("GDP","Happiness","Generosity"))
y_axis=st.selectbox("Select the data for the Y-axis",("GDP","Happiness","Generosity"))
st.subheader(f"{x_axis} and {y_axis}")
print(f"El valor de {x_axis} es: ")
print(df[f"{x_axis.lower()}"])
def get_data():
    x = df[f"{x_axis.lower()}"]
    y= df[f"{y_axis.lower()}"]
    return x,y

x,y = get_data()

figure = px.scatter(x=x, y=y)

st.plotly_chart(figure)
