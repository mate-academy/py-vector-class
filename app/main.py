from __future__ import annotations
from math import sqrt, degrees, acos, cos, sin, radians


class Vector:
    def __init__(self, x_cor: int, y_cor: int) -> None:
        self.x = round(x_cor, 2)
        self.y = round(y_cor, 2)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple,
            end_point: tuple) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return ValueError("Zero vector")
        return Vector(round(self.x / length, 2), round(self.y / length, 2))

    def angle_between(self, other: Vector) -> float:
        res_1 = self * other
        res_2 = self.get_length() * other.get_length()
        if res_2 == 0:
            return 0
        cos_a = res_1 / res_2
        return round(degrees(acos(cos_a)))

    def get_angle(self) -> float:
        if not self.x or not self.y:
            return 0
        vec = Vector(0, 1)
        return self.angle_between(vec)

    def rotate(self, rt: float) -> Vector:
        rd = radians(rt)
        x_new = self.x * cos(rd) - self.y * sin(rd)
        y_new = self.x * sin(rd) + self.y * cos(rd)
        return Vector(round(x_new, 2), round(y_new, 2))
