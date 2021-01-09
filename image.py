from skimage import io, color
import numpy as np

class Image:
    def __init__(self, path, number_of_colors, maximum_cells, FLOOD_FILL_TOLERANCE):
        self.number_of_colors = number_of_colors
        self.maximum_cells = maximum_cells
        self.FLOOD_FILL_TOLERANCE = FLOOD_FILL_TOLERANCE

        self.__rgb = np.array(io.imread(path), dtype=np.float64) / 255
        self.__lab = color.rgb2lab(self.__rgb)

        self.h, self.w, self.d = self.__rgb.shape

    @property
    def rgb(self):
        return self.__rgb

    @rgb.setter
    def rgb(self, arr):
        self.__rgb = arr
        self.__lab = color.rgb2lab(arr)

    @property
    def lab(self):
        return self.__lab

    @lab.setter
    def lab(self, arr):
        self.__lab = arr
        self.__rgb = color.lab2rgb(arr)
