from __future__ import annotations
import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    @classmethod
    def create_vector_by_two_points(cls, start: any, end: any) -> Vector:
        xxxxx = end[0] - start[0]
        yyyyy = end[1] - start[1]
        return cls(xxxxx, yyyyy)

    def __add__(self, other: any) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: any) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: any) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    def get_length(self) -> any:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: any) -> any:
        cos_angle = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> any:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: float) -> Vector:
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
