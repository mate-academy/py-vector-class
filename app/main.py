from __future__ import annotations
import math


class Vector:
    def __init__(self, x1: float = 0, y1: float = 0) -> None:
        self.x = round(x1, 2)
        self.y = round(y1, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x1=self.x + other.x,
            y1=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x1=self.x - other.x,
            y1=self.y - other.y
        )

    def __mul__(self, other: int | float | Vector) -> Vector | float | int:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(
            x1=self.x * other,
            y1=self.y * other
        )

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple) -> Vector:
        return Vector(
            x1=list(end_point)[0] - list(start_point)[0],
            y1=list(end_point)[1] - list(start_point)[1]
        )

    def get_length(self) -> int | float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            x1=self.x / self.get_length(),
            y1=self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> int:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return math.ceil(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        cos_a = self.y / self.get_length()
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degree: int) -> Vector:
        rd = math.radians(degree)
        return Vector(
            x1=self.x * math.cos(rd) - self.y * math.sin(rd),
            y1=self.x * math.sin(rd) + self.y * math.cos(rd)
        )
