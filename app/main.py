from __future__ import annotations

from math import cos, acos, sin, degrees, radians


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
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
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        dot_prod = self * other
        len_prod = self.get_length() * other.get_length()

        cos_a = max(-1.0, min(1.0, dot_prod / len_prod))
        return round(degrees(acos(cos_a)))

    def get_angle(self) -> int:
        return round(degrees(acos(self.y / self.get_length())))

    def rotate(self, degrees: int) -> Vector:
        in_radians = radians(degrees)

        return Vector(
            cos(in_radians) * self.x - sin(in_radians) * self.y,
            sin(in_radians) * self.x + cos(in_radians) * self.y
        )
