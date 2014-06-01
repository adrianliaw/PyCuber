"""
With this module, we can import 
the modules under the cube_solver.
Import this module in the solving modules
if you want to use color_converter.py, cube.py, sps.py
"""

import sys
path = sys.path[0]
path = path.split('/')
path = '/'.join(path[:-1])
sys.path.append(path)
__all__ = []