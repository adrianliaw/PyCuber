from gevent import monkey
monkey.patch_all()
from flask import Flask, render_template
from flask.ext.triangle import Triangle
from flask.ext.socketio import SocketIO, emit
from cfop import CFOPSolver
import pycuber as pc


app = Flask(__name__)
app.config["SECRET_KEY"] = "358fcd5a045e6a1f71e4e57e1709dc7184734255195700efe7980fb4"
Triangle(app)
socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template("main.html")


@socketio.on("random", namespace="/socket")
def random_cube():
    cube = pc.Cube()(pc.Algo().random())
    data = {}
    for face, fname in zip(map(cube.get_face, "LUFDRB"), "LUFDRB"):
        for x, row in enumerate(face):
            for y, square in enumerate(row):
                data["{0}{1}{2}".format(fname, x, y)] = {"background": square.colour}
    emit("random cube generated", data)


@socketio.on("cfop", namespace="/socket")
def solve_by_cfop(data):
    try:
        cube = pc.Cube(pc.array_to_cubies(data["cubies"]))
        solver = CFOPSolver(cube)
        for step in solver.solve():
            emit("step solved", {"step_name": step[0], "result": repr(step[1]).split()})
    except ValueError:
        emit("error", {"error": "Invalid Cube"})




if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0")

