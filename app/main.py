from __future__ import annotations
import math


class Vector:
    def __init__(self, x_c: float, y_c: float) -> None:
        self.x = round(x_c, 2)
        self.y = round(y_c, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x_c=self.x + other.x,
            y_c=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x_c=self.x - other.x,
            y_c=self.y - other.y
        )

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, (float, int)):
            return Vector(x_c=self.x * other, y_c=self.y * other)
        return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        x_c = end_point[0] - start_point[0]
        y_c = end_point[1] - start_point[1]
        return cls(x_c, y_c)

    def get_length(self) -> float:
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            x_c=round(self.x / self.get_length(), 2),
            y_c=round(self.y / self.get_length(), 2)
        )

    def angle_between(self, vector: Vector) -> int | float:
        cos_a = (self * vector) / (self.get_length() * vector.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int | float:
        y_axis = Vector(x_c=0, y_c=1)
        return self.angle_between(y_axis)

    def rotate(self, degrees: float | int) -> Vector:
        a_cos = math.cos(math.radians(degrees))
        a_sin = math.sin(math.radians(degrees))
        return Vector(
            x_c=self.x * a_cos - self.y * a_sin,
            y_c=self.x * a_sin + self.y * a_cos
        )
