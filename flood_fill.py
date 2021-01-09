class Flood_fill:
    def __init__(self, image):
        self.lab_pixels = image.lab
        self.w = image.w 
        self.h = image.h

        self.FLOOD_FILL_TOLERANCE = image.FLOOD_FILL_TOLERANCE
        self.number_of_colors = image.number_of_colors
        self.maximum_cells = image.maximum_cells

    def get_neighbours(self, index):
        height = index[0]
        width = index[1]
        neighbours = []
        
        up = (height + 1, width)
        down = (height - 1, width)
        left = (height, width - 1)
        right = (height, width + 1)

        for i in [up, down, left, right]:
            if 0 <= i[0] <= self.h - 1 and 0 <= i[1] <= self.w - 1:
                neighbours.append(i)

        return neighbours
    
    @staticmethod
    def color_distance(color1, color2):
        return (abs(color1[0]-color2[0])**2 + abs(color1[1]-color2[1])**2 + abs(color1[2]-color2[2])**2)**.5

    def flood(self, start_pixel, unplaced_pixels):
        queue = set({start_pixel})
        visited = set()
        cell = set()

        start_color = self.lab_pixels[start_pixel[0]][start_pixel[1]]

        while queue:
            pixel = queue.pop()
            if self.color_distance(start_color, self.lab_pixels[pixel[0]][pixel[1]]) < self.FLOOD_FILL_TOLERANCE:
                cell.add(pixel)
                unplaced_pixels.remove(pixel)

                for i in self.get_neighbours(pixel):
                    if (i in unplaced_pixels) and (i not in cell) and (i not in visited):
                        queue.add(i)
                        
            visited.add(pixel)
            
        return cell

