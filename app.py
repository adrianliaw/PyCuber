from flask import Flask, render_template
from flask_triangle import Triangle

app = Flask(__name__)
Triangle(app)

@app.route("/")
def index():
    return render_template("main.html")

def main():
    app.run("0.0.0.0")

if __name__ == "__main__":
    app.run(debug=True)
