from __future__ import annotations

import math


class Vector:
    def __init__(self, x_crd: float, y_crd: float) -> None:
        self.x = round(x_crd, 2)
        self.y = round(y_crd, 2)

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

    def __mul__(self, other: [Vector, float]) -> Vector:
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
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(
            self.x / length,
            self.y / length
        )

    def angle_between(self, other: Vector) -> int:
        len1 = self.get_length()
        len2 = other.get_length()
        cosine = self * other / (len1 * len2)
        return round(math.degrees(math.acos(cosine)))

    def get_angle(self) -> int:
        len1 = self.get_length()
        cosine = self.y / len1
        return round(math.degrees(math.acos(cosine)))

    def rotate(self, degrees: int) -> Vector:
        return Vector(
            math.cos(math.radians(degrees)) * self.x
            - math.sin(math.radians(degrees)) * self.y,
            math.sin(math.radians(degrees)) * self.x
            + math.cos(math.radians(degrees)) * self.y
        )
