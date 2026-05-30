import numpy as np
import random

from config import config
from deap   import creator, base

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

def random_color():
  r, g, b = [random.randint(0, 255) for _ in range(3)]
  a = random.randint(30, 255)
  return (r, g, b, a)

def random_coords():
  return [(random.random(), random.random()) for _ in range(config["points_per_polygon"])]

def random_shape():
  return {
    "coords": random_coords(),
    "color": random_color()
  }

def random_individual():
  return creator.Individual([random_shape() for _ in range(config["num_polygons"])])