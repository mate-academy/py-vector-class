from __future__ import annotations
from math import acos, cos, radians, sin, sqrt
from math import degrees as deg


class Vector:

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:

        return Vector(
            x_cor=end_point[0] - start_point[0],
            y_cor=end_point[1] - start_point[1]
        )

    def __init__(self, x_cor: int | float, y_cor: int | float) -> None:
        self.x_cor = round(x_cor, 2)
        self.y_cor = round(y_cor, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(x_cor=self.x_cor + other.x_cor,
                      y_cor=self.y_cor + other.y_cor)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(x_cor=self.x_cor - other.x_cor,
                      y_cor=self.y_cor - other.y_cor)

    def __mul__(self, other: int | float | Vector) -> Vector | float | int:
        if isinstance(other, (int, float)):
            return Vector(x_cor=other * self.x_cor, y_cor=other * self.y_cor)

        return self.x_cor * other.x_cor + self.y_cor * other.y_cor

    def get_length(self) -> int | float:
        return sqrt(self.x_cor ** 2 + self.y_cor ** 2)

    def get_normalized(self) -> Vector:

        return Vector(
            x_cor=self.x_cor / self.get_length(),
            y_cor=self.y_cor / self.get_length()
        )

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        len_product = self.get_length() * other.get_length()

        return round(deg(acos(dot_product / len_product)))

    def get_angle(self) -> int:
        vector_y = Vector(0, 1)

        return round(self.angle_between(vector_y))

    def rotate(self, degrees: int) -> Vector:
        rad_angle = radians(degrees)
        cos_angle = cos(rad_angle)
        sin_angle = sin(rad_angle)

        return Vector(
            x_cor=cos_angle * self.x_cor - sin_angle * self.y_cor,
            y_cor=sin_angle * self.x_cor + cos_angle * self.y_cor
        )
