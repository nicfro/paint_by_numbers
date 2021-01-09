import numpy as np

def mean_cell_color(cell, pixel_map):
    return np.array([pixel_map[pixel] for pixel in cell]).sum(axis=0)