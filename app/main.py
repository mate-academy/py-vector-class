from __future__ import annotations

import math


class Vector:
    def __init__(self, coordinate_x: float, coordinate_y: float) -> None:
        self.x = round(coordinate_x, 2)
        self.y = round(coordinate_y, 2)

    def __add__(self, other: Vector) -> Vector:
        self.x = round(self.x + other.x, 2)
        self.y = round(self.y + other.y, 2)
        return self

    def __sub__(self, other: Vector) -> Vector:
        self.x = round(self.x - other.x, 2)
        self.y = round(self.y - other.y, 2)
        return self

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            self.x = round(self.x * other, 2)
            self.y = round(self.y * other, 2)
        return self

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        coordinate_x = round(end_point[0] - start_point[0], 2)
        coordinate_y = round(end_point[1] - start_point[1], 2)
        return cls(coordinate_x, coordinate_y)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** (1 / 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        self.x = round(self.x / length, 2)
        self.y = round(self.y / length, 2)
        return self

    def angle_between(self, other: Vector) -> int:
        multiply_of_vectors = self.x * other.x + self.y * other.y
        angle = math.acos(
            multiply_of_vectors / (self.get_length() * other.get_length())
        )
        return round(math.degrees(angle))

    def get_angle(self) -> int:
        return round(
            math.degrees(math.acos(self.y / self.get_length()))
        )

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        new_x = round(
            math.cos(radians) * self.x
            - math.sin(radians) * self.y, 2
        )
        new_y = round(
            math.sin(radians) * self.x
            + math.cos(radians) * self.y, 2
        )
        self.x = new_x
        self.y = new_y
        return self
