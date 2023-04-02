from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: int | float, y_coord: int | float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        self.x = round(self.x + other.x, 2)
        self.y = round(self.y + other.y, 2)
        return self

    def __sub__(self, other: Vector) -> Vector:
        self.x = round(self.x - other.x, 2)
        self.y = round(self.y - other.y, 2)
        return self

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, (int, float)):
            self.x = round(self.x * other, 2)
            self.y = round(self.y * other, 2)
        else:
            dot_product = self.x * other.x + self.y * other.y
            return dot_product
        return self

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        vector1 = cls(*end_point)
        vector2 = cls(*start_point)
        return vector1 - vector2

    def get_length(self) -> float | int:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        self.x = round(self.x / length, 2)
        self.y = round(self.y / length, 2)
        return self

    def angle_between(self, other: Vector) -> int | float:
        length_self = self.get_length()  # the length of first vector
        length_other = other.get_length()  # the length of second vector
        dot_product = self.x * other.x + self.y * other.y
        cos_a = dot_product / (length_self * length_other)
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int | float:
        angle = math.atan2(self.x, self.y)
        return (
            math.degrees(angle)
            if angle >= 0 else round(360 - math.degrees(angle + 2 * math.pi))
        )

    def rotate(self, degrees: int | float) -> Vector:
        radians = math.radians(degrees)
        cos = math.cos(radians)
        sin = math.sin(radians)
        new_x = cos * self.x - sin * self.y
        new_y = sin * self.x + cos * self.y
        return Vector(new_x, new_y)
