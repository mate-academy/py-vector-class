from __future__ import annotations
import math


class Vector:
    def __init__(self, x_point: float, y_point: float) -> None:
        self.x = round(x_point, 2)
        self.y = round(y_point, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            dot_product = self.x * other.x + self.y * other.y
            return dot_product
        return Vector(
            round(self.x * other, 2),
            round(self.y * other, 2)
        )

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple) -> Vector:
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        length = math.sqrt(self.x ** 2 + self.y ** 2)
        return length

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length()
        )

    def angle_between(self, vector: Vector) -> int:
        angle = self * vector / (self.get_length() * vector.get_length())
        angle_in_degree = math.degrees(math.acos(angle))
        return round(angle_in_degree)

    def get_angle(self) -> int:
        vec = Vector(0, abs(self.y))
        angle = self * vec / (self.get_length() * vec.get_length())
        angle_in_degree = math.degrees(math.acos(angle))
        return round(angle_in_degree)

    def rotate(self, degree: int) -> Vector:
        degree = math.radians(degree)
        return Vector(
            self.x * math.cos(degree) - self.y * math.sin(degree),
            self.x * math.sin(degree) + self.y * math.cos(degree)
        )
