from __future__ import annotations
import math


class Vector:
    def __init__(self, x1: float, y1: float) -> None:
        self.x1 = round(x1, 2)
        self.y1 = round(y1, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x1 + other.x1, self.y1 + other.y1)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x1 - other.x1, self.y1 - other.y1)

    def __mul__(self, other: int | float | "Vector") -> "Vector" | float:
        # a · b = ax × bx + ay × by
        if isinstance(other, Vector):
            return self.x1 * other.x1 + self.y1 * other.y1
        return Vector(self.x1 * other, self.y1 * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> "Vector":
        x1 = end_point[0] - start_point[0]
        y1 = end_point[1] - start_point[1]
        return Vector(x1, y1)

    def get_length(self) -> float:
        return (self.x1 ** 2 + self.y1 ** 2) ** 0.5

    def get_normalized(self) -> "Vector":
        x1 = self.x1 / self.get_length()
        y1 = self.y1 / self.get_length()
        return Vector(x1, y1)

    def angle_between(self, vector: "Vector") -> int:
        dot_product = Vector.__mul__(self, vector)
        magnitude = self.get_length() * vector.get_length()
        cos = dot_product / magnitude
        return round(math.degrees(math.acos(cos)))

    def get_angle(self) -> int:
        y_axis = Vector(0, abs(self.y1))
        return self.angle_between(y_axis)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        x1 = self.x1 * math.cos(radians) - self.y1 * math.sin(radians)
        y1 = self.x1 * math.sin(radians) + self.y1 * math.cos(radians)
        return Vector(x1, y1)
