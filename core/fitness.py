import numpy as np
from utils.image import load_image
from config      import config
from PIL         import Image, ImageDraw

def draw_individual(individual):
  canvas = Image.new("RGBA", (config["image_size"][0], config["image_size"][1]), (255, 255, 255, 255))
  
  for shape in individual:
    layer = Image.new("RGBA", (config["image_size"][0], config["image_size"][1]), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer, "RGBA")
    
    color = shape["color"]
    pts = [
      (x * config["image_size"][0], y * config["image_size"][1])
      for (x, y) in shape["coords"]
    ]
    
    draw.polygon(pts, fill=color)
    
    canvas = Image.alpha_composite(canvas, layer)
  
  return np.array(canvas, dtype=np.uint8)

target = load_image() 

def mse(individual):
  return np.mean((individual.astype(np.float32) - target.astype(np.float32)) ** 2)

def evaluate(individual):
  rendered = draw_individual(individual)
  diff = mse(rendered)
  return diff,