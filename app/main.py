import math
from typing import Union


class Vector:
    def __init__(self, point_x: float, point_y: float) -> None:
        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x,
                      self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x,
                      self.y - other.y)

    def __mul__(self, other: "Vector") -> Union["Vector", float]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    begin_point: tuple,
                                    end_point: tuple) -> "Vector":
        return cls(*end_point) - cls(*begin_point)

    def get_length(self) -> float:
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def get_normalized(self) -> "Vector":
        return Vector(self.x / self.get_length(),
                      self.y / self.get_length())

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        cos_a = dot_product / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: float) -> "Vector":
        rads = math.radians(degrees)
        cos_theta = math.cos(rads)
        sin_theta = math.sin(rads)
        return Vector(self.x * cos_theta - self.y * sin_theta,
                      self.x * sin_theta + self.y * cos_theta)
