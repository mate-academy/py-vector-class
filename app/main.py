from __future__ import annotations
from math import sqrt, degrees, acos, cos, sin, radians


class Vector:
    def __init__(self, vector_x: int | float, vector_y: int | float) -> None:
        self.x = round(vector_x, 2)
        self.y = round(vector_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            vector_x=self.x + other.x,
            vector_y=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            vector_x=self.x - other.x,
            vector_y=self.y - other.y
        )

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        return Vector(
            vector_x=self.x * other,
            vector_y=self.y * other
        )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple) -> Vector:
        return cls(
            vector_x=end_point[0] - start_point[0],
            vector_y=end_point[1] - start_point[1]
        )

    def get_length(self) -> int | float:
        return sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        vector_len = self.get_length()
        return Vector(
            vector_x=self.x / vector_len,
            vector_y=self.y / vector_len
        )

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        vector_len = self.get_length() * other.get_length()
        return round(degrees(acos(dot_product / vector_len)))

    def get_angle(self) -> int:
        y_axis_vector = Vector(vector_x=0, vector_y=abs(self.y))
        return self.angle_between(y_axis_vector)

    def rotate(self, degree: int) -> Vector:
        radian = radians(degree)
        return Vector(
            vector_x=cos(radian) * self.x - sin(radian) * self.y,
            vector_y=sin(radian) * self.x + cos(radian) * self.y
        )
