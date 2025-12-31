from __future__ import annotations
from math import hypot, acos, pi, cos, sin, radians


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(round(self.x + other.x, 2), round(self.y + other.y, 2))

    def __sub__(self, other: Vector) -> Vector:
        return Vector(round(self.x - other.x, 2), round(self.y - other.y, 2))

    def __mul__(self, other: Vector | float) -> float:
        return self.x * other.x + self.y * other.y \
            if isinstance(other, Vector) \
            else Vector(round(self.x * other, 2), round(self.y * other, 2))

    def get_length(self) -> float:
        return hypot(self.x, self.y)

    def get_normalized(self) -> Vector:
        return Vector(
            round(self.x / self.get_length(), 2),
            round(self.y / self.get_length(), 2)
        )

    def angle_between(self, other: Vector) -> float:
        radians = acos((self.x * other.x + self.y * other.y)
                       / (self.get_length() * other.get_length()))
        return round(180 * radians / pi, 0)

    def get_angle(self) -> float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degree: int) -> Vector:
        degree = radians(degree)
        return Vector(
            round(cos(degree) * self.x - sin(degree) * self.y, 2),
            round(sin(degree) * self.x + cos(degree) * self.y, 2)
        )

    @staticmethod
    def create_vector_by_two_points(first: tuple, second: tuple) -> Vector:
        return Vector(
            round(second[0] - first[0], 2),
            round(second[1] - first[1], 2)
        )
