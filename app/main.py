from __future__ import annotations
import math
from typing import Any


class Vector:
    def __init__(self, coordinates_x: float, coordinates_y: float) -> None:
        self.x = round(coordinates_x, 2)
        self.y = round(coordinates_y, 2)

    def __add__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            raise TypeError("Can only add Vector to Vector")
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            raise TypeError("Can only sub Vector to Vector")
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Any) -> Any:
        if not isinstance(other, Vector):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple) -> Vector:
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(round(self.x / self.get_length(), 2),
                      round(self.y / self.get_length(), 2))

    def angle_between(self, other: Vector) -> int:
        cos_a = self.__mul__(other) / (self.get_length() * other.get_length())
        return math.ceil(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return int(math.degrees(math.acos(self.y / self.get_length())))

    def rotate(self, degrees: int) -> Vector:
        return Vector(
            (self.x * math.cos(math.radians(degrees))
             - self.y * math.sin(math.radians(degrees))),
            (self.x * math.sin(math.radians(degrees))
             + self.y * math.cos(math.radians(degrees)))
        )
