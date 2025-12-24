from __future__ import annotations
import math


class Vector:

    def __init__(self, x_dot: float, y_dot: float) -> None:
        self.x = round(x_dot, 2)
        self.y = round(y_dot, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.x + other.x,
            self.y + other.y,
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x - other.x,
            self.y - other.y,
        )

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(
                self.x * other,
                self.y * other,
            )

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple) -> "Vector":
        return cls(
            end[0] - start[0],
            end[1] - start[1],
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** .5

    def get_normalized(self) -> Vector:
        self_len = self.get_length()
        return Vector(
            self.x / self_len,
            self.y / self_len,
        )

    def angle_between(self, vector2: Vector) -> int:
        dot_product = self * vector2
        length_product = self.get_length() * vector2.get_length()
        cos_a = dot_product / length_product
        theta = math.degrees(math.acos(cos_a))
        return round(theta)

    def get_angle(self) -> int:
        sin_a = self.y / self.get_length()
        theta = math.degrees(math.acos(sin_a))
        return round(theta)

    def rotate(self, degree: int) -> Vector:
        return Vector(
            self.x * math.cos(math.radians(degree))
            - self.y * math.sin(math.radians(degree)),
            self.x * math.sin(math.radians(degree))
            + self.y * math.cos(math.radians(degree)),
        )
