import asyncio
import websockets
import json
import cfop
import pycuber as pc

@asyncio.coroutine
def ws_handler(websocket, path):
    if path == "/cfop":
        cube = yield from websocket.recv()
        try:
            cube = pc.Cube(pc.array_to_cubies(cube))
            solver = cfop.CFOPSolver(cube)
            for step in solver.solve():
                yield from websocket.send(json.dumps({
                    "step_name": step[0], 
                    "result": repr(step[1]).split(), 
                    }))
        except:
            yield from websocket.send(json.dumps({
                "error": "Invalid Cube", 
                }))
    elif path == "/random":
        yield from websocket.recv()
        cube = pc.Cube()(pc.Algo().random())
        data = {}
        for face, fname in zip(map(cube.get_face, "LUFDRB"), "LUFDRB"):
            for x, row in enumerate(face):
                for y, square in enumerate(row):
                    data["{0}{1}{2}".format(fname, x, y)] = {"background": square.colour}
        yield from websocket.send(json.dumps(data))


if __name__ == "__main__":
    from app import main
    from threading import Thread
    t = Thread(target=main)
    t.start()
    start_server = websockets.serve(ws_handler, "0.0.0.0", 8765)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

