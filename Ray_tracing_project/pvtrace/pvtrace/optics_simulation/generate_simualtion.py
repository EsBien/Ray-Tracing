""" before starting to run the project we need to generate
 the lens rays and drops """
from pvtrace import *
import time
import functools
import numpy as np
import random
import pandas as pd
import configparser
from pvtrace.light.light import default_wavelength

config = configparser.ConfigParser()
config.read('config.yaml')

xx = np.linspace(200, 800, 200)  # wavelength, units: nm
absorption_spectrum = lumogen_f_red_305.absorption(xx)  # units: nm-1
emission_spectrum = lumogen_f_red_305.emission(xx)
f_wavelength = config.getfloat('WAVELENGH', 'wavelengh_0')


world = Node(
    name="World",
    geometry=Sphere(
        radius=15.0,
        material=Material(refractive_index=1.0), ))


def generate_lenses(num_lenses):
    lenses = []
    for i in range(num_lenses):
        lens = Node(
            name="sphere (glass)" + str(i + 1),
            geometry=Sphere(
                radius=0.5,
                material=Material(refractive_index=1.5),
                isLen=True),
            parent=world, )
        lenses.append(lens)
    return lenses


def generate_rays(n, y_location_wavelengh):
    rays = []
    for i in range(n):
        ray = Node(
            name="ray (555nm)" + str(i),
            parent=world,
            light=Light(
                wavelength=functools.partial(default_wavelength, f_wavelength),
                #     direction=functools.partial(
                #         cone, np.radians(1.0)   )
            ))
        y_location_wavelengh += config.getfloat('LED_ARRAY', 'gap_between_led')
        ray.translate(
            (config.getfloat('LED', 'x_location'), y_location_wavelengh, config.getfloat('LED', 'x_location')))
        rays.append(ray)
    return rays


def generate_droplet_data(start, end):
    droplet_data = []
    for i in range(random.randint(start, end)):
        sphere = Node(name="sphere (glass)" + str(i + 7),
                      geometry=Sphere(
                          radius=random.uniform(0.2, 0.8),
                          stratTime=random.randint(0, 256),
                          material=Material(
                              refractive_index=config.getfloat('DROP', 'refractive_index'),
                              components=[
                                  Luminophore(
                                      emission=np.column_stack((xx, emission_spectrum)),
                                      quantum_yield=1.0,
                                      phase_function=isotropic,
                                      coefficient=1.0),
                                  Absorber(coefficient=0.1)
                              ]), ),
                      parent=world)
        sphere.location = (-50, 0, 0)
        sphere.geometry._y_Location = random.uniform(-0.5, 0.5)
        sphere.geometry._z_Location = random.uniform(0, 4)
        droplet_data.append(sphere)
    return droplet_data
