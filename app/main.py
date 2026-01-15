from __future__ import annotations
from math import acos, degrees, radians, sin, cos


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))

        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return (
            Vector(
                end_point[0] - start_point[0], end_point[1] - start_point[1]
            )
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        upper_part = self * other
        footer_part = self.get_length() * other.get_length()
        arg_cos = acos(upper_part / footer_part)
        arg_cos_degrees = degrees(arg_cos)
        return int(round(arg_cos_degrees, 0))

    def get_angle(self) -> int:
        vector1 = Vector(0, 1)
        upper_part = self * vector1
        footer_part = self.get_length() * vector1.get_length()
        arg_cos_result = acos(upper_part / footer_part)
        arg_cos_degrees = degrees(arg_cos_result)
        return int(round(arg_cos_degrees, 0))

    def rotate(self, degree: int) -> Vector:
        radian = radians(degree)
        new_x = self.x * cos(radian) - self.y * sin(radian)
        new_y = self.x * sin(radian) + self.y * cos(radian)
        return Vector(new_x, new_y)
