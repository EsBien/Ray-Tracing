import matplotlib as plt
from pvtrace.optics_simulation.generate_simualtion import *

array_of_wavelengh = []
rays = []
droplet_data = []  # list with the liquids drop that fall
csv_data = []
y_location_wavelengh = config.getfloat('LED', 'y_location')
frame = 0
x = 0
y = np.exp(-((xx - 600.0) / 50.0) ** 2)


def gPower(strat_time, frame):
    secend = int((frame - strat_time // 32))
    return secend * (9.8 / 32) / 100


# Create a specified number of lenses to simulate water droplets
lenses = generate_lenses(6)

# lenses[0].location = (config.getfloat('LEN', 'lenses[0]_xlocation'), config.getfloat('LEN', 'lenses[0]_ylocation'),
#                  config.getfloat('LEN', 'lenses[0]_zlocation'))
lenses[0].location = (0.0, 0.5, 6)

lenses[1].location = (0.0, -0.5, 6)

lenses[2].location = (0.0, 1.5, 5.5)

lenses[3].location = (0.0, -1.5, 5.5)

lenses[4].location = (0.0, 2.5, 5)

lenses[5].location = (0.0, -2.5, 5)  # Add source of photons

for key in config['WAVELENGH']:
    array_of_wavelengh.append(config.getfloat('WAVELENGH', key))

""" Create a specified number of rays to simulate water droplets"""
rays = generate_rays(20, y_location_wavelengh)
# Use meshcat to render the scene (optional)
viewer = MeshcatRenderer(open_browser=True, transparency=False, opacity=0.5, wireframe=True)
scene = Scene(world)
viewer.render(scene)
# material=Material(
#             refractive_index=1.5,
#             components=[
#                 Luminophore(
#                     emission=np.column_stack((_x, emission_spectrum)),
#                     quantum_yield=1.0,
#                     phase_function=isotropic,
#                     coefficient=1.0
# refractive_index=config.getfloat('DROP','refractive_index'),
#                 ),
droplet_data=generate_droplet_data(20,40)
droplet_data.sort(key=lambda x: x.geometry._startTime, reverse=False)
# for i in droplet_data:
#     print(i.geometry._startTime)

time.sleep(0.5)
current_second = 0
while droplet_data:
    scene = Scene(world)
    viewer.render(scene)
    for l in rays:
        l.light.wavelength = functools.partial(default_wavelength,
                                               array_of_wavelengh[frame // 32 % len(array_of_wavelengh)])
    for ball in droplet_data:
        if ball.geometry._x_Location > 15:
            droplet_data.remove(ball)
        if ball.geometry._startTime <= frame:
            ball.location = (ball.geometry._x_Location, ball.geometry._y_Location, ball.geometry._z_Location)
            ball.geometry._x_Location += gPower(ball.geometry._startTime, frame)
        if ball.geometry._startTime >= frame:
            ball.location = (ball.geometry._x_Location, ball.geometry._y_Location, ball.geometry._z_Location)
    for lens in lenses:
        lens.geometry._color = 0
        lens.geometry.set_collision = 0

    for ray in scene.emit(20):
        # ray.direction(0.08,-0.34,-0.94)
        history = photon_tracer.follow(scene, ray)
        path, events = zip(*history)
        viewer.add_ray_path(path)
    for lens in lenses:
        if lens.geometry.collision:
            lens.geometry._color = lens.geometry._color / lens.geometry.set_collision

    csv_data += [
        {'len': 'lenses[0]', 'num_of_ray_hit': "" + str(lenses[0].geometry.collision), 'time': "" + str(frame),
         "color": '' + str(lenses[0].geometry._color)},
        {'len': 'lenses[1]', 'num_of_ray_hit': "" + str(lenses[1].geometry.collision), 'time': "" + str(frame),
         "color": '' + str(lenses[1].geometry._color)},
        {'len': 'lenses[2]', 'num_of_ray_hit': "" + str(lenses[2].geometry.collision), 'time': "" + str(frame),
         "color": '' + str(lenses[2].geometry._color)},
        {'len': 'lenses[3]', 'num_of_ray_hit': "" + str(lenses[3].geometry.collision), 'time': "" + str(frame),
         "color": '' + str(lenses[3].geometry._color)},
        {'len': 'lenses[4]', 'num_of_ray_hit': "" + str(lenses[4].geometry.collision), 'time': "" + str(frame),
         "color": '' + str(lenses[4].geometry._color)},
        {'len': 'len0', 'num_of_ray_hit': '' + str(lenses[5].geometry.collision), 'time': '' + str(frame),
         "color": '' + str(lenses[5].geometry._color)}]

    print("lenses[0]", lenses[0].geometry.collision)
    print("lenses[1]", lenses[1].geometry.collision)
    print("lenses[2]", lenses[2].geometry.collision)
    print("lenses[3]", lenses[3].geometry.collision)
    print("lenses[4]", lenses[4].geometry.collision)
    print("lenses[5]", lenses[5].geometry.collision)
    frame += 1
    viewer.remove(scene.emit(num_rays=1))

df = pd.DataFrame(csv_data)
df.to_csv("data1.csv")

plt.plot(xx, y)
plt.xlabel('Wavelength (nm)')
plt.grid(linestyle='dotted')
dist = Distribution(xx, y)
dist.sample(np.random.uniform())
light = Light(
    wavelength=lambda: dist.sample(np.random.uniform())
)
plt.show()
while True:
    try:
        time.sleep(0.1)
    except KeyboardInterrupt:
        break
