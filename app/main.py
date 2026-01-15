from __future__ import annotations
from math import sqrt, degrees, acos, cos, sin, radians


class Vector:
    def __init__(self, xx: float, yy: float) -> None:
        self.x = round(xx, 2)
        self.y = round(yy, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        le = self.get_length()
        return Vector(self.x / le, self.y / le)

    def angle_between(self, vector: Vector) -> int:
        dot_product = self * vector
        vectors_mul = self.get_length() * vector.get_length()
        return round(degrees(acos(dot_product / vectors_mul)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, angle: int) -> Vector:
        new_x = self.x * cos(radians(angle)) - self.y * sin(radians(angle))
        new_y = self.x * sin(radians(angle)) + self.y * cos(radians(angle))

        return Vector(new_x, new_y)
