from __future__ import annotations
from typing import Callable
import math


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Callable) -> Callable:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Callable) -> Callable:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, coefficient: float) -> Callable:
        if isinstance(coefficient, Vector):
            return self.x * coefficient.x + self.y * coefficient.y
        return Vector(
            round(self.x * coefficient, 2),
            round(self.y * coefficient, 2))

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Callable:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Callable:
        return Vector(
            self.x * (1 / self.get_length()),
            self.y * (1 / self.get_length()))

    def angle_between(self, vector: Callable) -> int:
        return round(math.acos((self * vector)
                               / (self.get_length() * vector.get_length()))
                     * 180 / math.pi)

    def get_angle(self) -> int:
        vector = Vector(0, 1)
        return self.angle_between(vector)

    def rotate(self, degree: int) -> Callable:
        degree = degree / 180 * math.pi
        return Vector(
            math.cos(degree) * self.x - math.sin(degree) * self.y,
            math.sin(degree) * self.x + math.cos(degree) * self.y)
