from __future__ import annotations

import math


class Vector:
    def __init__(self, coordinate_x: int, coordinate_y: int) -> None:
        self.x = round(coordinate_x, 2)
        self.y = round(coordinate_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(
                self.x * other,
                self.y * other
            )

    @classmethod
    def create_vector_by_two_points(cls,
                                    first: tuple,
                                    second: tuple) -> Vector:
        return Vector(
            second[0] - first[0],
            second[1] - first[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            round(self.x / self.get_length(), 2),
            round(self.y / self.get_length(), 2)
        )

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def angle_between(self, other: Vector) -> float | int:
        return round(math.degrees(math.acos(
            (self.x * other.x + self.y * other.y)
            / (self.get_length() * other.get_length()))))

    def get_angle(self) -> float:
        y_axis_x = 0
        y_axis_y = 1

        dot = self.x * y_axis_x + self.y * y_axis_y
        length = math.sqrt(self.x ** 2 + self.y ** 2)
        cos_theta = dot / length

        angle = math.degrees(math.acos(cos_theta))

        return round(angle)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)

        new_x = round(self.x * math.cos(radians)
                      - self.y * math.sin(radians), 2)
        new_y = round(self.x * math.sin(radians)
                      + self.y * math.cos(radians), 2)

        return Vector(new_x, new_y)
