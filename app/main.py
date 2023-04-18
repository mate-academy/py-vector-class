from __future__ import annotations
from math import sqrt


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

    def __mul__(self, other: float | Vector) -> float | Vector:
        if isinstance(other, float | int):
            return Vector(
                x=self.x * other,
                y=self.y * other
            )
        else:
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0], end_point[1] - start_point[1])

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self):
        return Vector(
            x=self.x * (1 / self.get_length()),
            y=self.y * (1 / self.get_length())
        )

    # def angle_between(self, vector: Vector) :