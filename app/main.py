from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: int | float, y_coord: int | float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x + (other.x * -1),
            self.y + (other.y * -1)
        )

    def __mul__(self, other: Vector | int | float) -> Vector:
        # a · b = ax × bx + ay × by
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(
                round(self.x * other, 2),
                round(self.y * other, 2)
            )

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        return Vector(*end_point) - Vector(*start_point)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> int:
        cos_a = self * other / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        cos_deg = math.cos(math.radians(degrees))
        sin_deg = math.sin(math.radians(degrees))
        return Vector(
            cos_deg * self.x - sin_deg * self.y,
            sin_deg * self.x + cos_deg * self.y
        )
