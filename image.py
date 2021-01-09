from skimage import io, color
import numpy as np

class Image:
    def __init__(self, path, number_of_colors, maximum_cells, FLOOD_FILL_TOLERANCE):
        self.number_of_colors = number_of_colors
        self.maximum_cells = maximum_cells
        self.FLOOD_FILL_TOLERANCE = FLOOD_FILL_TOLERANCE

        self.rgb = np.array(io.imread(path), dtype=np.float64) / 255
        self.lab = color.rgb2lab(self.rgb)

        self.h, self.w, self.d = self.rgb.shape
        
        self.cell_sets = {}
        self.lab_pixel_map = {}
        self.unplaced_pixels = set()
        for i in range(self.h):
            for j in range(self.w):
                self.lab_pixel_map[(i,j)] = self.lab[i][j]
                self.unplaced_pixels.add((i,j))

        self.cell_map = {}