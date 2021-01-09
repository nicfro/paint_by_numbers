import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.utils import shuffle
from time import time
from skimage import io
from image import Image
from flood_fill import Flood_fill
import copy

img = Image("flood.png", 20, 100, 10)

image = img.lab
'''
flattened_image_array = image.reshape((-1,img.d))

t0 = time()
flattened_image_array_sample = shuffle(flattened_image_array, random_state=0)[0:1000]
kmeans = KMeans(n_clusters=img.number_of_colors, random_state=0).fit(flattened_image_array_sample)
img.lab = kmeans.cluster_centers_[kmeans.predict(flattened_image_array)].reshape(image.shape)
print("done in %0.3fs." % (time() - t0))
'''
cell_sets = {}
color_pixel_dict = {}
unplaced_pixels = set()
for i in range(img.h):
    for j in range(img.w):
        color_pixel_dict[(i,j)] = image[i][j]
        unplaced_pixels.add((i,j))

flood_fill = Flood_fill(img)

counter = 1
while unplaced_pixels:
    start_pixel = unplaced_pixels.pop()
    unplaced_pixels.add(start_pixel)

    cell = flood_fill.flood(start_pixel, unplaced_pixels)

    cell_sets[counter] = cell
    for pixel in cell:
        color_pixel_dict[pixel] = counter
    
    counter += 1



plt.clf()
plt.axis('off')
plt.title(f'Quantized image ({img.number_of_colors} colors, K-Means)')
plt.imshow(img.rgb)

plt.show()