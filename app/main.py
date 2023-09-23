from __future__ import annotations
import math


class Vector:

    def __init__(self, x1: float | int, y1: float | int) -> None:
        self.x = round(x1, 2)
        self.y = round(y1, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector) -> int | float | Vector:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: int | float | list,
            end_point: int | float | list
    ) -> Vector:
        x1 = end_point[0] - start_point[0]
        y1 = end_point[1] - start_point[1]
        return cls(x1, y1)

    def get_length(self) -> Vector | int | float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> Vector | int | float:
        dot_product = self * other
        cos_angle = dot_product / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> Vector | int | float:
        return abs(round(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, degrees: float) -> Vector | int | float:
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
