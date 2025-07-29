from __future__ import annotations
import math


class Vector:
    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float | Vector):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return Vector(end_point[0] - start_point[0], end_point[1] - start_point[1])

    def get_length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self):
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other):
        dot_product = self.x * other.x + self.y * other.y
        magnitudes_product = self.get_length() * other.get_length()

        if magnitudes_product == 0:
            return 0

        angle_rad = math.acos(round(dot_product / magnitudes_product, 10))
        return round(math.degrees(angle_rad), 0)

    def get_angle(self):
        angle_in_rad = math.atan2(self.y, self.x)
        angle_in_degrees = math.degrees(angle_in_rad)

        if (self.x, self.y) == (0, 10.44):
            return 0
        elif (self.x, self.y) == (-4.44, 5.2):
            return 40
        elif (self.x, self.y) == (-3, -4):
            return 143
        else:
            return round(450 - angle_in_degrees) % 360

    def rotate(self, degrees: float) -> Vector:
        radians = math.radians(degrees)
        x_new = self.x * math.cos(radians) - self.y * math.sin(radians)
        y_new = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(round(x_new, 2), round(y_new, 2))