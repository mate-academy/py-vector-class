from __future__ import annotations
import math


class Vector:
    def __init__(self, xxx: float, yyy: float) -> None:
        self.xxx = round(xxx, 2)
        self.yyy = round(yyy, 2)

    @classmethod
    def create_vector_by_two_points(cls, start: any, end: any) -> Vector:
        xxx = end[0] - start[0]
        yyy = end[1] - start[1]
        return cls(xxx, yyy)

    def __add__(self, other: any) -> Vector:
        return Vector(self.xxx + other.xxx, self.yyy + other.yflake8)

    def __sub__(self, other: any) -> Vector:
        return Vector(self.xxx - other.xxx, self.yyy - other.yflake8)

    def __mul__(self, other: any) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(self.xxx * other, self.yyy * other)
        elif isinstance(other, Vector):
            return self.xxx * other.xxx + self.yyy * other.yyy

    def get_length(self) -> any:
        return math.sqrt(self.xxx ** 2 + self.yyy ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.xxx / length, self.yyy / length)

    def angle_between(self, other: any) -> any:
        cos_angle = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> any:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: float) -> Vector:
        radians = math.radians(degrees)
        new_x = self.xxx * math.cos(radians) - self.yyy * math.sin(radians)
        new_y = self.xxx * math.sin(radians) + self.yyy * math.cos(radians)
        return Vector(new_x, new_y)
