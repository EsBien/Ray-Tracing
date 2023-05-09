import time
import sys
import functools
import numpy as np

from pvtrace import *
lsc = LSC((5.0, 5.0, 1.0))  # size in cm
lsc.show()                  # open visualiser
lsc.simulate(100)           # emit 100 rays
lsc.report()                # print report
# world = Node(
#     name="world (air)",
#     geometry=Sphere(
#         radius=10.0,
#         material=Material(refractive_index=1.0),
#     ),
# )

arr = np.array([1,2,3],dtype=float)
print(arr)