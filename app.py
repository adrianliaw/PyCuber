from flask import Flask, render_template
import asyncio, websockets

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("main.html")

if __name__ == "__main__":
    app.run()
