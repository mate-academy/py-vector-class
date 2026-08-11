from __future__ import annotations
import math


class Vector:
    def __init__(self, vector_x: float | int, vector_y: float | int) -> None:
        self.x = round(vector_x, 2)
        self.y = round(vector_y, 2)

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

    def __mul__(self, other: float | int | Vector) -> float | int | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        return Vector(
            round(self.x * other, 2),
            round(self.y * other, 2),
        )

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple) -> Vector:
        return Vector(
            end[0] - start[0],
            end[1] - start[1]
        )

    def get_length(self) -> float | int:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        vector_length = self.get_length()

        return Vector(
            self.x / vector_length,
            self.y / vector_length
        )

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        self_length = self.get_length()
        other_length = other.get_length()

        cos_a = dot_product / (self_length * other_length)
        angle = math.degrees(math.acos(cos_a))

        return round(angle)

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)

        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)

        self.x = round(new_x, 2)
        self.y = round(new_y, 2)
        return self
