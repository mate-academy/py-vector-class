from __future__ import annotations
from math import sqrt, acos, degrees, cos, sin, radians


class Vector:
    def __init__(self, x: float | int, y: float | int) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x=self.x + other.x,
            y=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x=self.x - other.x,
            y=self.y - other.y
        )

    def __mul__(self, other: Vector | float | int) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(
            x=self.x * other,
            y=self.y * other
        )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return Vector(
            x=end_point[0] - start_point[0],
            y=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(
            x=round(self.x / length, 2),
            y=round(self.y / length, 2),
        )

    def angle_between(self, other: Vector) -> int:
        return round(
            degrees(
                acos(self * other / (self.get_length() * other.get_length()))
            )
        )

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, abs(self.y)))

    def rotate(self, deg: int) -> Vector:
        theta = radians(deg)
        return Vector(
            x=self.x * cos(theta) - self.y * sin(theta),
            y=self.x * sin(theta) + self.y * cos(theta)
        )
