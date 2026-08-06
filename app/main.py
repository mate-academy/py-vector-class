from __future__ import annotations
import math


class Vector:

    def __init__(self, x: float, y: float) -> None:
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

    def __mul__(self, other: Vector | float) -> Vector | float:
        return self.x * other.x \
            + self.y * other.y \
            if isinstance(other, Vector) \
            else Vector(
                x=round(self.x * other, 2),
                y=round(self.y * other, 2)
            )

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple,
        end_point: tuple
    ) -> Vector:
        return Vector(
            x=round(end_point[0] - start_point[0], 2),
            y=round(end_point[1] - start_point[1], 2)
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            x=round(self.x / self.get_length(), 2),
            y=round(self.y / self.get_length(), 2)
        )

    def angle_between(self, other: Vector) -> int:
        mul_result = self * other
        len_mult_result = self.get_length() * other.get_length()
        return round(math.degrees(math.acos(mul_result / len_mult_result)), 0)

    def get_angle(self) -> int:
        return self.angle_between(
            other=Vector(x=0, y=20)
        )

    @staticmethod
    def get_sin(degree: int) -> float:
        return math.sin(math.radians(degree))

    @staticmethod
    def get_cos(degree: int) -> float:
        return math.cos(math.radians(degree))

    def rotate(self, degree: int) -> Vector:
        return Vector(
            x=round((self.x * Vector.get_cos(degree))
                    - (self.y * Vector.get_sin(degree)), 2),
            y=round((self.x * Vector.get_sin(degree))
                    + (self.y * Vector.get_cos(degree)), 2)
        )
