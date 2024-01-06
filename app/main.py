from __future__ import annotations

import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x=self.x + other.x,
            y=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x=self.x - other.x,
            y=self.y - other.y
        )

    def __mul__(self, other: float | int | Vector) -> Vector | float:
        if isinstance(other, (float | int)):
            return Vector(
                x=self.x * other,
                y=self.y * other
            )
        return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            x=end_point[0] - start_point[0],
            y=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            x=self.x / self.get_length(),
            y=self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> int:
        return int(
            round(
                math.degrees(
                    math.acos(
                        self.__mul__(other)
                        / (self.get_length()
                           * other.get_length()))
                ),
                0
            )
        )

    def get_angle(self) -> int:
        y_vector = Vector(0, 5)
        return self.angle_between(y_vector)

    def rotate(self, degrees: int) -> Vector:
        return Vector(
            x=math.cos(math.radians(degrees)) * self.x
            - math.sin(math.radians(degrees)) * self.y,
            y=math.sin(math.radians(degrees)) * self.x
            + math.cos(math.radians(degrees)) * self.y
        )
