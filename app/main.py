from __future__ import annotations

import math


class Vector:

    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector) is True:
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector) is True:
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, int | float) is True:
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector) is True:
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple)\
            -> Vector:
        vector = cls(end_point[0] - start_point[0]
                     , end_point[1] - start_point[1])
        if isinstance(vector, Vector) is True:
            return vector

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(round(self.x / Vector.get_length(self), 2)
                      , round(self.y / Vector.get_length(self), 2))

    def angle_between(self, other: Vector) -> float:
        if isinstance(other, Vector) is True:
            cos_a = Vector.__mul__(self, other) / (Vector.get_length(self)
                                                   * Vector.get_length(other))
            return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return round(Vector.angle_between(self, Vector(0, 1)))

    def rotate(self, degrees: int) -> Vector:
        x_2 = round(math.cos(math.radians(degrees)) * self.x
                    - math.sin(math.radians(degrees)) * self.y, 2)
        y_2 = round(math.sin(math.radians(degrees)) * self.x
                    + math.cos(math.radians(degrees)) * self.y, 2)
        return Vector(x_2, y_2)
