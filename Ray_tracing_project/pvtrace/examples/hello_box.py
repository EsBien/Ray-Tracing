import time
import sys
import functools
import numpy as np

from pvtrace import *
import logging
logging.getLogger('trimesh').setLevel(logging.CRITICAL)

world = Node(
    name="world (air)",
    geometry=Sphere(
        radius=50.0,
        material=Material(refractive_index=1.0),
    )
)


box = Node(
    name="sphere (glass)",
    geometry=Box(
        (10.0, 10.0, 1.0),
        material=Material(refractive_index=1.5),
    ),
    parent=world
)

light = Node(
    name="Light (555nm)",
    light=Light(),
    parent=world
)
light.rotate(np.radians(60), (1.0, 0.0, 0.0))

renderer = MeshcatRenderer(
    zmq_url="tcp://127.0.0.1:6000", wireframe=True, open_browser=True
)
start_t = time.time()
scene = Scene(world)
renderer.render(scene)
for ray in scene.emit(100):
    steps = photon_tracer.follow(scene, ray)
    path, events = zip(*steps)
    renderer.add_ray_path(path)
    time.sleep(0.1)

print(f"Took {time.time() - start_t}s to trace 100 rays.")
# //***********************

# Wait for Ctrl-C to terminate the script; keep the window open
print("Ctrl-C to close")
while True:
    try:
        time.sleep(0.3)
    except KeyboardInterrupt:
        sys.exit()
