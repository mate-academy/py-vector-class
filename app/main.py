from __future__ import annotations
from math import sqrt, cos, sin, degrees, acos, radians


class Vector:
    def __init__(self, first: int | float, second: int | float) -> None:
        self.x = round(first, 2)
        self.y = round(second, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            first=self.x + other.x,
            second=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            first=self.x - other.x,
            second=self.y - other.y
        )

    def __mul__(self, other: Vector | float | int) -> Vector | float | int:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        return Vector(
            first=self.x * other,
            second=self.y * other
        )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:

        return cls(
            first=end_point[0] - start_point[0],
            second=end_point[1] - start_point[1]
        )

    def get_length(self) -> float | int:
        return sqrt(
            self.x ** 2 + self.y ** 2
        )

    def get_normalized(self) -> Vector:
        vector_length = self.get_length()

        return Vector(
            first=self.x / vector_length,
            second=self.y / vector_length
        )

    def angle_between(self, other: Vector) -> int:
        vectors_product = self * other

        return round(
            degrees(
                acos(
                    vectors_product / (self.get_length() * other.get_length())
                )
            )
        )

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees_: int) -> Vector:
        radi = radians(degrees_)
        return Vector(
            first=self.x * cos(radi) - self.y * sin(radi),
            second=self.x * sin(radi) + self.y * cos(radi)
        )
