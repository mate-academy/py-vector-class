from __future__ import annotations

import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        x_coord = self.x + other.x
        y_coord = self.y + other.y

        return Vector(x_coord, y_coord)

    def __sub__(self, other: Vector) -> Vector:
        x_coord = self.x - other.x
        y_coord = self.y - other.y

        return Vector(x_coord, y_coord)

    def __mul__(self, other: float | Vector) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        x_coord = self.x * other
        y_coord = self.y * other

        return Vector(x_coord, y_coord)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:

        x_coord = end_point[0] - start_point[0]
        y_coord = end_point[1] - start_point[1]

        return cls(x_coord, y_coord)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return self * (1 / self.get_length())

    def angle_between(self, other: Vector) -> int:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        degrees = math.degrees(math.acos(cos_a))
        return round(degrees)

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        x_coord = (self.x * math.cos(radians)
                   - self.y * math.sin(radians))
        y_coord = (self.x * math.sin(radians)
                   + self.y * math.cos(radians))

        return Vector(x_coord, y_coord)
