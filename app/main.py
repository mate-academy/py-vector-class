from __future__ import annotations
from math import sqrt, degrees, acos, radians, cos, sin


class Vector:
    def __init__(self, x: float, y: float) -> None:  # noqa: VNE001
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float | int | Vector) -> Vector | float:
        if isinstance(other, float | int):
            return Vector(self.x * other, self.y * other)
        return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, vector: Vector) -> int:
        dot = self.__mul__(vector)
        length_a = self.get_length()
        length_b = vector.get_length()
        cos_theta = dot / (length_a * length_b)
        cos_theta = max(-1, min(1, cos_theta))
        return round(degrees(acos(cos_theta)))

    def get_angle(self) -> int:
        norm = self.get_length()
        if norm == 0:
            raise ValueError
        cos_theta = self.y / norm
        cos_theta = max(-1.0, min(1.0, cos_theta))
        return round(degrees(acos(cos_theta)))

    def rotate(self, degrees: int) -> Vector:
        theta = radians(degrees)
        return Vector(self.x * cos(theta) - self.y * sin(theta), self.x
                      * sin(theta) + self.y * cos(theta))
