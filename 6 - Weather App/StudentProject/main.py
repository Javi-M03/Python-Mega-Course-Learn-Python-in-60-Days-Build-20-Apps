from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home_sp.html")

@app.route("/api/v1/<word>/")
def about(word):
    definition = word.upper()
    return {"word":word,
            "definition": definition}

app.run(debug=True)

if __name__ == "__main__":
    app.run(debug = True)