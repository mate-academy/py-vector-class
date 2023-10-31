from __future__ import annotations
import math


class Vector:

    def __init__(self, x1: float, y1: float) -> None:
        self.x = round(x1, 2)
        self.y = round(y1, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float | int) -> Vector | float:
        if not isinstance(other, Vector):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(round(end_point[0] - start_point[0], 2),
                   round(end_point[1] - start_point[1], 2))

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        cos_alpha = ((self.__mul__(other))
                     / (self.get_length() * other.get_length()))
        return int(round(math.degrees(math.acos(cos_alpha)), 0))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 10))

    def rotate(self, degrees: int) -> Vector:
        x_new = (math.cos(math.radians(degrees)) * self.x
                 - math.sin(math.radians(degrees)) * self.y)
        y_new = ((math.sin(math.radians(degrees)) * self.x)
                 + math.cos(math.radians(degrees)) * self.y)
        return Vector(x_new, y_new)
