from __future__ import annotations

import math


class Vector:
    def __init__(self, axis_x: float, axis_y: float) -> None:
        self.x = round(axis_x, 2)
        self.y = round(axis_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            axis_x=self.x + other.x,
            axis_y=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            axis_x=self.x - other.x,
            axis_y=self.y - other.y
        )

    def __mul__(self, other: Vector | int) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(
                axis_x=self.x * other,
                axis_y=self.y * other
            )

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0], end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> int:
        return round(
            math.degrees(
                math.acos(self.__mul__(other)
                          / (self.get_length() * other.get_length()))
            )
        )

    def get_angle(self) -> int:
        return round(math.degrees(math.acos(self.y / self.get_length())))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        return Vector(
            axis_x=self.x * math.cos(radians) - self.y * math.sin(radians),
            axis_y=self.x * math.sin(radians) + self.y * math.cos(radians)
        )
