from __future__ import annotations

import math


class Vector:

    def __init__(self, point_x: float, point_y: float) -> None:
        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, other: Vector | float) -> float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x * self.x
                         + self.y * self.y)

    def get_normalized(self) -> Vector:
        return Vector(
            round(self.x / self.get_length(), 2),
            round(self.y / self.get_length(), 2)
        )

    def angle_between(self, other: Vector) -> int:
        return math.ceil(
            math.degrees(
                math.acos(self.__mul__(other)
                          / self.get_length()
                          / other.get_length()))
        )

    def get_angle(self) -> int:
        return math.trunc(math.degrees(math.acos(self.y
                                                 / self.get_length())))

    def rotate(self, degrees: int) -> Vector:
        return Vector(round(
            math.cos(math.radians(degrees)) * self.x
            - math.sin(math.radians(degrees)) * self.y, 2),
            round(math.sin(math.radians(degrees)) * self.x
                  + math.cos(math.radians(degrees)) * self.y, 2))
