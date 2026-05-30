import numpy as np
import os

from config import config
from PIL    import Image

def load_image():
  img = Image.open(config["target"])
  img = img.convert("RGBA")

  height, width = config["image_size"][0], config["image_size"][1]
  img = img.resize((width, height))

  return np.array(img, dtype=np.uint8)

def save_image(array, path):
  img = Image.fromarray(array.astype(np.uint8), "RGBA")
  os.makedirs(os.path.dirname(path), exist_ok=True)
  img.save(path)