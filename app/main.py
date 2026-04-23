from __future__ import annotations

import math


class Vector:
    def __init__(self, vector_x: float, vector_y: float) -> None:
        self.x = round(vector_x, 2)
        self.y = round(vector_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other + self.y * other
        return Vector(self.x * other.x, self.y * other.y)

    def __truediv__(self, scalar: float) -> Vector:
        return Vector(round(self.x / scalar, 2), round(self.y / scalar, 2))

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    @classmethod
    def create_vector_by_two_points(
        cls, start: tuple[float, float], end: tuple[float, float]
    ) -> Vector:
        return cls(end[0] - start[0], end[1] - start[1])

    def get_length(self) -> float:
        return round(math.sqrt(self.x ** 2 + self.y ** 2), 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(round(self.x / length, 2), round(self.y / length, 2))

    def angle_between(self, other: Vector) -> int:
        cos_angle = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> int:
        return round(math.degrees(math.atan2(self.x, self.y)))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(round(new_x, 2), round(new_y, 2))
