from __future__ import annotations

from math import radians, sin, cos, degrees, acos


class Vector:
    def __init__(self, x: int | float, y: int | float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float | Vector) -> float | Vector:
        if isinstance(other, Vector):
            dot_product = self.x * other.x + self.y * other.y
            return dot_product
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        mul = self.__mul__(other)
        le = self.get_length() * other.get_length()
        return round(degrees(acos(mul / le)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 8))

    def rotate(self, angle: int) -> Vector:
        x_2 = cos(radians(angle)) * self.x - sin(radians(angle)) * self.y
        y_2 = sin(radians(angle)) * self.x + cos(radians(angle)) * self.y
        return Vector(x_2, y_2)
