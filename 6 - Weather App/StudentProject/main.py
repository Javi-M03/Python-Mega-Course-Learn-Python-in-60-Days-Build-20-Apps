from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
df = pd.read_csv("dictionary.csv")

@app.route("/")
def home():
    return render_template("home_sp.html")

@app.route("/api/v1/<word>/")
def about(word):
    definition = df.loc[df['word'] == word]['definition'].squeeze()
    return {"word":word,
            "definition": definition}

app.run(debug=True)

if __name__ == "__main__":
    app.run(debug = True)