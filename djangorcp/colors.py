import random
import math
from colorsys import hsv_to_rgb

class ColorGenerator:
    colors = []

    def get_random_color_set(self, s=None, v=None):
        self.saturation = s
        self.value = v

        for i in range(0,24):
            color = self.generate_new_color()
            self.colors.append(color)

        return ['#%02X%02X%02X' % c for c in self.colors]

    def get_random_hsv(self):
        r = lambda: random.random()

        h = r()
        s = self.saturation if self.saturation else r()
        v = self.value if self.value else r()

        return (h, s, v)

    def get_distance(self, color):
        h_distance = (self.colors[-1][0]*360 + 180) - color[0]*360
        s_distance = 1 - (self.colors[-1][1] - color[1])
        v_distance = 1 - (self.colors[-1][2] - color[2])

        return abs(h_distance * s_distance * v_distance)

    def get_best_distance(self, color, current_best):
        distance = self.get_distance(color)
        return distance if not current_best else min(distance, current_best)


    def generate_new_color(self):
        best_distance = None
        best_color = None

        # Generate 100 color sample and pick the most diverse color.
        for i in range(0,100):
            color = self.get_random_hsv()

            if not self.colors:
                return color

            # Make sure we dont get the same color again.
            while color == self.colors[-1]:
                color = self.get_random_hsv()

            # Test the color towards existing colors to find a not to alike color.
            distance = self.get_best_distance(color, best_distance)

            if distance == best_distance or not best_distance:
                best_distance = distance
                best_color = color

        # Convert hsv coordinates to rgb coordinates
        h,s,v = best_color
        rgb_cords = hsv_to_rgb(h, s, v)

        # Convert rgb coordinates to rgb value
        rgb = tuple([int(math.floor(255*r)) for r in rgb_cords])
        return rgb
