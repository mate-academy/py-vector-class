from __future__ import annotations

import math


class Vector:

    def __init__(self, ax: float, by: float) -> None:
        self.x = round(ax, 2)
        self.y = round(by, 2)

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

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        return Vector(
            self.x * other,
            self.y * other
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        # a = 1 / self.get_length()
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> float:
        return round(math.degrees(math.acos((self * other)
                                            / (self.get_length()
                                               * other.get_length()))), 0)

    def get_angle(self) -> float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, angle: float) -> Vector:
        cosi = math.cos(math.radians(angle))
        sinu = math.sin(math.radians(angle))
        return Vector(
            cosi * self.x - sinu * self.y,
            sinu * self.x + cosi * self.y,
        )

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(list(end_point)[0] - list(start_point)[0],
                   list(end_point)[1] - list(start_point)[1])
