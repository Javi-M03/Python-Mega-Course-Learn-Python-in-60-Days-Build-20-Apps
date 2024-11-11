import streamlit as st
import plotly.express as px
from nltk.sentiment import SentimentIntensityAnalyzer
import glob


analyzer = SentimentIntensityAnalyzer()

filepaths = sorted(glob.glob("diary/*.txt"))
print(filepaths)



positivity = []
negativity = []
for filepath in filepaths:
    print(filepath)
    with open(filepath) as file:
        content = file.read()
    analysis = analyzer.polarity_scores(content)
    positivity.append(analysis["pos"])
    negativity.append(analysis["neg"])

dates = [name.strip(".txt").strip("diary/") for name in filepaths]
print(dates)

st.title("Diary Tone")
st.subheader("Positivity")
pos_figure = px.line(x=dates, y=positivity,labels={"x":"Date","y":"Positivity"})
st.plotly_chart(pos_figure)


st.subheader("Negativity")
neg_figure = px.line(x=dates, y=negativity,labels={"x":"Date","y":"Negativity"})
st.plotly_chart(neg_figure)

