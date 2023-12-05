from __future__ import annotations
import math


class Vector:
    def __init__(self, xflake8: float, yflake8: float) -> None:
        self.xflake8 = round(xflake8, 2)
        self.yflake8 = round(yflake8, 2)

    @classmethod
    def create_vector_by_two_points(cls, start: any, end: any) -> Vector:
        xflake8 = end[0] - start[0]
        yflake8 = end[1] - start[1]
        return cls(xflake8, yflake8)

    def __add__(self, other: any) -> Vector:
        return Vector(self.xflake8 + other.xflake8, self.yflake8 + other.yflake8)

    def __sub__(self, other: any) -> Vector:
        return Vector(self.xflake8 - other.xflake8, self.yflake8 - other.yflake8)

    def __mul__(self, other: any) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(self.xflake8 * other, self.yflake8 * other)
        elif isinstance(other, Vector):
            return self.xflake8 * other.xflake8 + self.yflake8 * other.yflake8

    def get_length(self) -> any:
        return math.sqrt(self.xflake8 ** 2 + self.yflake8 ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.xflake8 / length, self.yflake8 / length)

    def angle_between(self, other: any) -> any:
        cos_angle = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> any:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: float) -> Vector:
        radians = math.radians(degrees)
        new_x = self.xflake8 * math.cos(radians) - self.yflake8 * math.sin(radians)
        new_y = self.xflake8 * math.sin(radians) + self.yflake8 * math.cos(radians)
        return Vector(new_x, new_y)
