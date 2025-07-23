from __future__ import annotations
import math


class Vector:
    def __init__(self, x: float | int, y: float | int) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        raise TypeError("Expected a Vector type")

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        raise TypeError("Expected a Vector type")

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, int) or isinstance(other, float):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        raise TypeError("Expected a Vector, int or float type")

    @classmethod
    def create_vector_by_two_points(cls, point1: tuple, point2: tuple) -> Vector:
        if isinstance(point1, tuple) and isinstance(point1, tuple):
            return cls((point2[0] - point1[0]), (point2[1] - point1[1]))
        raise TypeError("Expected tuple types")

    def get_length(self) -> float | int:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        if isinstance(other, Vector):
            return round(
                math.degrees(math.acos(self.__mul__(other) / (self.get_length() * other.get_length())))
            )
        raise TypeError("Expected a Vector type")

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, angle: int) -> Vector:
        if isinstance(angle, int):
            return Vector(
                (self.x * math.cos(math.radians(angle)) - self.y * math.sin(math.radians(angle))),
                (self.x * math.sin(math.radians(angle)) + self.y * math.cos(math.radians(angle)))
            )
