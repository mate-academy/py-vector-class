from typing import Union
from math import sqrt, pow
import math


class Vector:

    def __init__(self, x_c: float, y_c: float) -> None:
        self.x_c = round(x_c, 2)
        self.y_c = round(y_c, 2)

    @property
    def x(self) -> float:
        return self.x_c

    @property
    def y(self) -> float:
        return self.y_c

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(other.x_c + self.x_c, other.y_c + self.y_c)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x_c - other.x_c, self.y_c - other.y_c)

    def __mul__(self, other: Union[int, float, "Vector"]) \
            -> Union[float, "Vector"]:
        if isinstance(other, (int, float)):
            return Vector(self.x_c * other, self.y_c * other)
        elif isinstance(other, Vector):
            return (self.x_c * other.x_c) + (self.y_c * other.y_c)

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple) -> "Vector":
        return cls(end[0] - start[0], end[1] - start[1])

    def get_length(self) -> float:
        return sqrt(pow(self.x_c, 2) + pow(self.y_c, 2))

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize a zero-length vector")
        return Vector(self.x_c / length, self.y_c / length)

    def angle_between(self, other: "Vector") -> float:
        dot_product = self * other
        lengths_product = self.get_length() * other.get_length()

        if lengths_product == 0:
            raise ValueError("Error")

        cos_theta = dot_product / lengths_product
        angle = round(math.degrees(math.acos(cos_theta)))

        return angle

    def get_angle(self) -> float:
        cos_theta = self.y_c / self.get_length()
        return round(math.degrees(math.acos(cos_theta)))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)

        x_rot = self.x_c * math.cos(radians) - self.y_c * math.sin(radians)
        y_rot = self.x_c * math.sin(radians) + self.y_c * math.cos(radians)

        return Vector(round(x_rot, 2), round(y_rot, 2))
