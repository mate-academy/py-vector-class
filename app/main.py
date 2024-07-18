from __future__ import annotations
import math


class Vector:
    def __init__(self, xxx: float, yyy: float) -> None:
        self.x = round(xxx, 2)
        self.y = round(yyy, 2)

    def __add__(self, other: Vector | float) -> Vector:
        if isinstance(other, Vector):
            return Vector(
                self.x + other.x,
                self.y + other.y
            )
        return Vector(
            self.x + other,
            self.y + other
        )

    def __sub__(self, other: Vector | float) -> Vector:
        if isinstance(other, Vector):
            return Vector(
                self.x - other.x,
                self.y - other.y
            )
        return Vector(
            self.x - other,
            self.y - other
        )

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(
            self.x * other,
            self.y * other
        )

    @classmethod
    def create_vector_by_two_points(
            cls, point_1: tuple, point_2: tuple) -> Vector:
        return cls(
            point_2[0] - point_1[0],
            point_2[1] - point_1[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

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
