from __future__ import annotations
import math


class Vector:
    def __init__(self, l_x: int | float, l_y: int | float) -> None:
        self.x = round(l_x, 2)
        self.y = round(l_y, 2)

    def __add__(self, other: Vector) -> Vector:
        sum_x = self.x + other.x
        sum_y = self.y + other.y
        return Vector(sum_x, sum_y)

    def __sub__(self, other: Vector) -> Vector:
        sub_x = self.x - other.x
        sub_y = self.y - other.y
        return Vector(sub_x, sub_y)

    def __mul__(self, other: int | float | Vector) -> Vector | int | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        l_x = round(self.x * other, 2)
        l_y = round(self.y * other, 2)
        return Vector(l_x, l_y)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: int | float,
            end_point: int | float) -> Vector:
        cls.x = end_point[0] - start_point[0]
        cls.y = end_point[1] - start_point[1]
        return Vector(cls.x, cls.y)

    def get_length(self) -> int | float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        dot_product = self.x * other.x + self.y * other.y
        module = self.get_length() * other.get_length()
        cos_a = dot_product / module
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        cos_a = self.y / self.get_length()
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: int | float) -> Vector:
        cos = math.cos(math.radians(degrees))
        sin = math.sin(math.radians(degrees))
        l_x = cos * self.x - sin * self.y
        l_y = sin * self.x + cos * self.y
        return Vector(l_x, l_y)
