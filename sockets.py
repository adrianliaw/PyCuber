import asyncio
import websockets
import json
import cfop
import pycuber as pc

@asyncio.coroutine
def ws_handler(websocket, path):
    if path == "/cfop":
        cube = yield from websocket.recv()
        cube = pc.Cube(pc.array_to_cubies(cube))
        try:
            solver = cfop.CFOPSolver(cube)
            for step in solver.solve():
                print(step)
                yield from websocket.send(json.dumps({
                    "step_name": step[0], 
                    "result": repr(step[1]).split(), 
                    }))
        except ValueError:
            yield from websocket.send(json.dumps({
                "error": "InvalidCube", 
                }))

start_server = websockets.serve(ws_handler, "127.0.0.1", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

