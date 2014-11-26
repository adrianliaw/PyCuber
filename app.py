from flask import Flask, render_template
from flask_triangle import Triangle

app = Flask(__name__)
Triangle(app)

@app.route("/")
def index():
    print(True)
    return render_template("main.html")

if __name__ == "__main__":
    app.run()
