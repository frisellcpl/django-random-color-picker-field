import random
import math


def get_random_color_set():
    colors = []

    for i in range(0,24):
        color = generate_new_color(colors)
        colors.append(color)

    return ['#%02X%02X%02X' % c for c in colors]


def get_random_color():
    r = lambda: random.randint(0,255)
    return (r(), r(), r())


def color_distance(c1,c2):
    return sum([abs(x[0]-x[1]) for x in zip(c1,c2)])


def generate_new_color(existing_colors):
    max_distance = None
    best_color = None

    for i in range(0,100):
        color = get_random_color()

        if not existing_colors:
            return color

        # Test the color towards existing colors to find a not to alike color.
        best_distance = min([color_distance(color,c) for c in existing_colors])

        if not max_distance or best_distance > max_distance:
            max_distance = best_distance
            best_color = color

        return best_color
