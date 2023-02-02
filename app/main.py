from __future__ import annotations

import math


class Vector:
    def __init__(self, x_: int | float, y_: int | float) -> None:
        self.x = round(x_, 2)
        self.y = round(y_, 2)

    def __add__(self, other: Vector | int | float) -> Vector | int | float:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector | int | float) -> Vector | int | float:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, int | float):
            return Vector(
                round(self.x * other, 2),
                round(self.y * other, 2)
            )
        dot_product = self.x * other.x + self.y * other.y
        return dot_product

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
        return Vector(round((self.x / self.get_length()), 2),
                      round((self.y / self.get_length()), 2))

    def angle_between(self, other: float | Vector) -> int:
        cos_a = (self.__mul__(other) / (self.get_length()
                                        * other.get_length()))
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        cos_a = (self.y / self.get_length())
        return int(math.degrees(math.acos(cos_a)))

    def rotate(self, angle: int) -> Vector:
        return Vector(
            round((self.x * (math.cos(math.radians(angle)))
                   - self.y * (math.sin(math.radians(angle)))), 2),
            round((self.y * (math.cos(math.radians(angle)))
                   + self.x * (math.sin(math.radians(angle)))), 2)
        )
