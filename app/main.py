from __future__ import annotations
import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | "Vector") -> "Vector" | float:
        # a · b = ax × bx + ay × by
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple) -> "Vector":
        x = end_point[0] - start_point[0]
        y = end_point[1] - start_point[1]
        return Vector(x, y)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> "Vector":
        x = self.x / self.get_length()
        y = self.y / self.get_length()
        return Vector(x, y)

    def angle_between(self, vector: "Vector") -> int:
        dot_product = Vector.__mul__(self, vector)
        magnitude = self.get_length() * vector.get_length()
        cos = dot_product / magnitude
        return round(math.degrees(math.acos(cos)))

    def get_angle(self) -> int:
        y_axis = Vector(0, abs(self.y))
        return self.angle_between(y_axis)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        x = self.x * math.cos(radians) - self.y * math.sin(radians)
        y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(x, y)
