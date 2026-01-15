from __future__ import annotations
from math import sqrt, acos, degrees, sin, cos, radians


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

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

    def __mul__(self, other: Vector | float | int) -> Vector | float:
        if isinstance(other, (float, int)):
            return Vector(
                self.x * other,
                self.y * other
            )
        return self.x * other.x + self.y * other.y

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
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> int:
        angle_cos = self * other / (self.get_length() * other.get_length())
        return round(degrees(acos(angle_cos)))

    def get_angle(self) -> int:
        cos_angle = self.y / self.get_length()
        return round(degrees(acos(cos_angle)))

    def rotate(self, angle: int) -> Vector:
        radian = radians(angle)
        return Vector(
            self.x * cos(radian) - self.y * sin(radian),
            self.y * cos(radian) + self.x * sin(radian)
        )
