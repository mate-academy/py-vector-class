from __future__ import annotations
from math import cos
from math import sin
from math import radians
from math import degrees
from math import acos


class Vector:

    def __init__(self, x_coord: int | float, y_coord: int | float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector | int | float) -> Vector:
        if not isinstance(other, (Vector, int, float)):
            raise TypeError(f"Cannot add vector of type {type(other)}")
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            return Vector(self.x + other, self.y + other)

    def __sub__(self, other: Vector | int | float) -> Vector:
        if not isinstance(other, (Vector, int, float)):
            raise TypeError(f"Cannot substrate vector of type {type(other)}")
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        else:
            return Vector(self.x - other, self.y - other)

    def __mul__(self, other: Vector | int | float) -> Vector | int:
        if not isinstance(other, (Vector, int, float)):
            raise TypeError(f"Cannot multiply vector of type {type(other)}")
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point:
                                    tuple[int | float, int | float],
                                    end_point: tuple[int | float, int | float]
                                    ) -> Vector:
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        calc_angle = (self * other) / (self.get_length() * other.get_length())
        return round(degrees(acos(calc_angle)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, angle: int) -> Vector:
        return Vector(
            cos(radians(angle)) * self.x - sin(radians(angle)) * self.y,
            sin(radians(angle)) * self.x + cos(radians(angle)) * self.y)
