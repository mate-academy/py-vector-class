from __future__ import annotations
from typing import Tuple
import math


class Vector:
    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __repr__(self) -> str:
        return f"(x: {self.x}, y:{self.y})"

    def __add__(self, other: Vector):
        if isinstance(other, Vector):
            x = self.x + other.x
            y = self.y + other.y
            return Vector(x, y)

    def __sub__(self, other: Vector):
        if isinstance(other, Vector):
            x = self.x - other.x
            y = self.y - other.y
            return Vector(x, y)

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, Vector):
            x = self.x * other.x
            y = self.y * other.y
            return x + y

        x = round(self.x * other, 2)
        y = round(self.y * other, 2)
        return Vector(x, y)

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: Tuple[int, int], end_point: Tuple[int, int]
    ) -> Vector:
        x = end_point[0] - start_point[0]
        y = end_point[1] - start_point[1]

        return Vector(x, y)

    def get_length(self):
        return (self.x**2 + self.y**2) ** 0.5

    def get_normalized(self) -> Vector:
        vector_len = self.get_length()
        x = self.x / vector_len
        y = self.y / vector_len
        return Vector(x, y)


def print_r(label, result):
    print(f"{label}: {result}")


start_point = (5.2, 2.6)
end_point = (10.7, 6)

vector = Vector.create_vector_by_two_points(start_point, end_point)
print_r("isinstance(vector, Vector)", isinstance(vector, Vector) is True)
print_r("vector", vector)
print_r("vector.x == 5.5", vector.x == 5.5)
print_r("vector.y == 3.4", vector.y == 3.4)
