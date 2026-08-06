from __future__ import annotations
import math


class Vector:

    def __init__(self, x_point: float, y_point: float) -> None:
        self.x = round(x_point, 2)
        self.y = round(y_point, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: int | Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> float | Vector:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        product = self * other
        len_self = self.get_length()
        len_other = other.get_length()
        cosine = product / (len_self * len_other)
        return round(math.degrees(math.acos(cosine)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        math1 = self.x * math.cos(math.radians(degrees))
        math2 = self.y * math.sin(math.radians(degrees))
        math3 = self.x * math.sin(math.radians(degrees))
        math4 = self.y * math.cos(math.radians(degrees))

        return Vector(
            math1 - math2,
            math3 + math4
        )
