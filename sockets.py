import asyncio
import websockets
import cfop
import pycuber as pc

@asyncio.coroutine
def cfop_solve(websocket, path):
    cube = yield from websocket.recv()
    cube = pc.Cube(cube)
    solver = cfop.CFOPSolver(cube)
    for step in solver.solve():
        yield from websocket.send(str(step))

start_server = websockets.serve(cfop_solve, "127.0.0.1", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

