import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.utils import shuffle
from time import time
from skimage import io
from image import Image
from flood_fill import Flood_fill
from merger import mean_cell_color
import copy
bear = "images/bear.jpg"
fish = "images/fish.jp"
flood = "images/flood.png"
img = Image(bear, 20, 100, 10)

'''
image = img.lab

flattened_image_array = image.reshape((-1,img.d))

t0 = time()
flattened_image_array_sample = shuffle(flattened_image_array, random_state=0)[0:1000]
kmeans = KMeans(n_clusters=img.number_of_colors, random_state=0).fit(flattened_image_array_sample)
img.lab = kmeans.cluster_centers_[kmeans.predict(flattened_image_array)].reshape(image.shape)
print("done in %0.3fs." % (time() - t0))
'''


flood_fill = Flood_fill(img)

counter = 1
while img.unplaced_pixels:
    start_pixel = img.unplaced_pixels.pop()
    img.unplaced_pixels.add(start_pixel)

    cell = flood_fill.flood(start_pixel)

    img.cell_sets[counter] = cell
    for pixel in cell:
        img.cell_map[pixel] = counter
    
    counter += 1

mean_cell_color = mean_cell_color(img.cell_sets[1], img.lab_pixel_map)


plt.clf()
plt.axis('off')
plt.title(f'Quantized image ({img.number_of_colors} colors, K-Means)')
plt.imshow(img.rgb)

plt.show()