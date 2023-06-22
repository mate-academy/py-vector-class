from __future__ import annotations
import math
from typing import Union


class Vector:
    # write your code here
    def __init__(self,
                 var_x: Union[int, float],
                 var_y: Union[int, float]) -> None:
        self.x = round(var_x, 2)
        self.y = round(var_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            var_x=self.x + other.x,
            var_y=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            var_x=self.x - other.x,
            var_y=self.y - other.y
        )

    def __mul__(self, other: Vector | Union[int, float]) -> Vector | float:

        if not isinstance(other, Vector):
            return Vector(
                var_x=self.x * other,
                var_y=self.y * other
            )
        elif isinstance(other, Vector):
            mult = self.x * other.x + self.y * other.y
            return mult

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:

        result = [
            end_point[i] - start_point[i]
            for i in range(len(start_point))
        ]

        return Vector(
            var_x=result[0],
            var_y=result[1]
        )

    def get_length(self) -> float:
        result = (self.x**2 + self.y**2)**0.5
        return result

    def get_normalized(self) -> Vector:
        invr = 1 / self.get_length()

        return Vector(
            var_x=self.x * invr,
            var_y=self.y * invr
        )

    def angle_between(self, other: Vector) -> int:
        mul_uv = self.x * other.x + self.y * other.y
        mod_uv = (self.x**2 + self.y**2)**0.5 * (other.x**2 + other.y**2)**0.5
        degree = mul_uv / mod_uv

        result = round(math.degrees(math.acos(degree)))
        return result

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, grad: int) -> Vector:
        ang = math.radians(grad)

        rotated_x = self.x * math.cos(ang) - self.y * math.sin(ang)
        rotated_y = self.x * math.sin(ang) + self.y * math.cos(ang)

        return Vector(
            var_x=rotated_x,
            var_y=rotated_y
        )
