from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: float | int, y_coord: float | int) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(round(self.x * other, 2), round(self.y * other, 2))

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        return cls(end_point[0] - start_point[0], end_point[1] - start_point[1])

    def get_length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self):
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other):
        cos_angle = (self * other) / (self.get_length() * other.get_length())
        angle = math.degrees(math.acos(cos_angle))
        return round(angle)

    def get_angle(self) -> int:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degrees):
        radians = math.radians(degrees)
        x_new = self.x * math.cos(radians) - self.y * math.sin(radians)
        y_new = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(round(x_new, 2), round(y_new, 2))
