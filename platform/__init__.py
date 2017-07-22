from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("main.html")

@app.route('/interests')
def interests():
    return render_template("interests.html")


if __name__ == "__main__":
    app.run()
