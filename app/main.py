from __future__ import annotations

import math
from math import sqrt, pow


class Vector:
    def __init__(
            self,
            x_coord: float,
            y_coord: float
    ) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x_coord=self.x + other.x,
            y_coord=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x_coord=self.x - other.x,
            y_coord=self.y - other.y
        )

    def __mul__(self, other: float | Vector) -> float | Vector:
        if type(other) == float or type(other) == int:
            return Vector(
                x_coord=round(self.x * other, 2),
                y_coord=round(self.y * other, 2)
            )
        elif type(other) == Vector:
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[float, float],
            end_point: tuple[float, float]
    ) -> Vector:
        return cls(
            x_coord=end_point[0] - start_point[0],
            y_coord=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return sqrt(pow(self.x, 2) + pow(self.y, 2))

    def get_normalized(self) -> Vector:
        return Vector(
            x_coord=round(self.x / self.get_length(), 2),
            y_coord=round(self.y / self.get_length(), 2)
        )

    def angle_between(self, other_vector: Vector) -> float:

        return round(math.degrees(math.acos(
            (self.x * other_vector.x + self.y * other_vector.y)
            / (self.get_length() * other_vector.get_length())
        )))

    def get_angle(self) -> float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)

        return Vector(
            self.x * math.cos(radians) - self.y * math.sin(radians),
            self.x * math.sin(radians) + self.y * math.cos(radians)
        )
