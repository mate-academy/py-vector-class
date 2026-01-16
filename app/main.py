from __future__ import annotations
import math


class Vector:

    def __init__(self, xc: int | float, yc: int | float) -> None:
        self.x = round(xc, 2)
        self.y = round(yc, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> int | float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, vector: Vector) -> int:
        product = self * vector
        len_product = self.get_length() * vector.get_length()
        cos_a = product / len_product
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        product = self.y
        len_product = self.get_length()
        cos_a = product / len_product
        return round(math.degrees(math.acos(cos_a)))

    def get_angle_x(self) -> int:
        product = self.x
        len_product = self.get_length()
        cos_a = product / len_product
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: int) -> Vector:
        diff = math.radians(degrees)
        cos_diff = math.cos(diff)
        sin_diff = math.sin(diff)
        rotated_x = (self.x * cos_diff) - (self.y * sin_diff)
        rotated_y = (self.x * sin_diff) + (cos_diff * self.y)
        return Vector(rotated_x, rotated_y)
