import random
import copy

from core.individual import random_color, random_coords, random_shape

def mutate_color(shape, sigma=25):
  r, g, b, a = shape["color"]
  new_color = (
    int(max(0, min(255, r + random.gauss(0, sigma)))),
    int(max(0, min(255, g + random.gauss(0, sigma)))),
    int(max(0, min(255, b + random.gauss(0, sigma)))),
    int(max(30, min(255, a + random.gauss(0, sigma/2)))),
  )
  shape["color"] = new_color
  return shape

def mutate_position(shape, magnitude=0.1):
  new_pts = []
  for x, y in shape["coords"]:
    dx, dy = random.uniform(-magnitude, magnitude), random.uniform(-magnitude, magnitude)
    new_pts.append((min(max(0, x + dx), 1), min(max(0, y + dy), 1)))

  shape["coords"] = new_pts

  return shape

def mutate_individual(individual, prob=0.1):
  mutant = copy.deepcopy(individual)

  for i in range(len(mutant)):
    if random.random() < prob:
      op = random.choice(["color", "position", "replace"])
      if op == "color":
          mutant[i] = mutate_color(mutant[i])
      elif op == "position":
          mutant[i] = mutate_position(mutant[i])
      elif op == "replace":
          mutant[i] = random_shape()

  return mutant,
