from __future__ import annotations
from math import acos
from math import degrees
from math import radians
from math import cos
from math import sin


class Vector:

    def __init__(self, x_coord: int | float, y_coord: int | float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(self, Vector) and isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(self, Vector) and isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(self, Vector) and isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(self, Vector) and isinstance(other, int | float):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> int | float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(),
                      self.y / self.get_length())

    def angle_between(self, other: Vector) -> int | float:
        return round(degrees(acos((self * other)
                                  / (self.get_length() * other.get_length()))))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, abs(self.y)))

    def rotate(self, deg: int) -> Vector:
        return Vector(self.x * cos(radians(deg)) - self.y * sin(radians(deg)),
                      self.y * cos(radians(deg)) + self.x * sin(radians(deg)))
