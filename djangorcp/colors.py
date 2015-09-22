import random
import math

class ColorGenerator:
    colors = []

    def get_random_color_set(self, s=None, v=None):
        self.saturation = s
        self.value = v

        for i in range(0,24):
            color = self.generate_new_color()
            print(color)
            self.colors.append(color)

        return ['#%02X%02X%02X' % c for c in self.colors]

    def get_random_hsv(self):
        r = lambda: random.random()

        h = random.randint(0, 360)
        s = self.saturation if self.saturation else r()
        v = self.value if self.value else r()

        return (h, s, v)

    def get_distance(self, color):
        h_distance = (self.colors[-1][0] + 180) - color[0]
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
        return tuple(self.hsv_to_rgb(h,s,v))

    def hsv_to_rgb(self, h, s, v):
        # One might as himself why I don't use colorsys here.
        # Well, just out of stupidity i guess. And I wanted to implement the
        # algorithm found at https://en.wikipedia.org/wiki/HSL_and_HSV as
        # readable as possible.

        h = float(h)
        s = float(s)
        v = float(v)
        c = v * s
        hi = h / 60.0
        x = c * (1- abs(hi % 2 - 1))
        m = v - c
        r,g,b = 0,0,0

        if 0 <= hi < 1: r,g,b = c, x, 0
        elif 1 <= hi < 2: r,g,b = x, c, 0
        elif 2 <= hi < 3: r,g,b = 0, c, x
        elif 3 <= hi < 4: r,g,b = 0, x, c
        elif 4 <= hi < 5: r,g,b = x, 0, c
        elif 5 <= hi < 6: r,g,b = c, 0, x

        return map(self.from_float, (r+m,g+m,b+m))

    def from_float(self, value, domain=255):
        return int(round(value * domain))
