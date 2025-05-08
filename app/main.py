from __future__ import annotations

import math


class Vector:
    def __init__(self, x_obj: float, y_obj: float) -> None:
        self.x = round(x_obj, 2)
        self.y = round(y_obj, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, number: float | Vector) -> Vector | float:
        if isinstance(number, Vector):
            return self.x * number.x + self.y * number.y
        return Vector(self.x * number, self.y * number)

    @classmethod
    def create_vector_by_two_points(cls, point1: tuple,
                                    point2: tuple) -> Vector:
        return cls.__sub__(Vector(point2[0], point2[1]),
                           Vector(point1[0], point1[1]))

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        return int(
            round(
                math.degrees(
                    math.acos(
                        self.__mul__(other) / (self.get_length()
                                               * other.get_length())
                    )
                ),
            )
        )

    def get_angle(self) -> int:
        return int(
            round(
                math.degrees(
                    math.acos(
                        self.y / self.get_length()
                    )
                ),
            )
        )

    def rotate(self, degrees: float) -> Vector:
        radians = math.radians(degrees)
        cos = math.cos(radians)
        sin = math.sin(radians)
        return Vector(
            round(self.x * cos - self.y * sin, 2),
            round(self.x * sin + self.y * cos, 2),
        )
