from __future__ import annotations

import math


class Vector:
    def __init__(self, x_coord: float | int, y_coord: float | int) -> None:
        self.x_coord = round(x_coord, 2)
        self.y_coord = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(
                self.x_coord + other.x_coord,
                self.y_coord + other.y_coord
            )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x_coord - other.x_coord,
            self.y_coord - other.y_coord
        )

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x_coord * other.x_coord + self.y_coord * other.y_coord
        return Vector(self.x_coord * other, self.y_coord * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple
                                    ) -> Vector:
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x_coord ** 2 + self.y_coord ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return self * (1 / length)

    def angle_between(self, other: Vector) -> int:
        cos_a = self * other / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> object:
        return Vector(
            self.x_coord * math.cos(math.radians(degrees))
            - self.y_coord * math.sin(math.radians(degrees)),
            self.x_coord * math.sin(math.radians(degrees))
            + self.y_coord * math.cos(math.radians(degrees))
        )
