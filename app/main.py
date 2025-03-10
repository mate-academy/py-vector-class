from __future__ import annotations
import math


class Vector:

    def __init__(self, vector_x: int | float, vector_y: int | float) -> None:
        self.x = round(vector_x, 2)
        self.y = round(vector_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(round(self.x + other.x, 2), round(self.y + other.y, 2))

    def __sub__(self, other: Vector) -> Vector:
        return Vector(round(self.x - other.x, 2), round(self.y - other.y, 2))

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, Vector):
            dot_product = (self.x * other.x) + (self.y * other.y)
            return dot_product
        else:
            return Vector(round(self.x * other, 2), round(self.y * other, 2))

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        return Vector(
            end_point[0] - start_point[0], end_point[1] - start_point[1]
        )

    def get_length(self) -> int | float:
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(round(self.x / length, 2), round(self.y / length, 2))

    def angle_between(self, other: Vector) -> int | float:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        degrees = math.degrees(
            math.atan2(self.y, self.x)
        )
        return round((degrees - 90) % 360)

    def rotate(self, degrees: int) -> Vector:
        cos_angle = math.cos(math.radians(degrees))
        sin_angle = math.sin(math.radians(degrees))
        x_rotated = self.x * cos_angle - self.y * sin_angle
        y_rotated = self.x * sin_angle + self.y * cos_angle
        return Vector(round(x_rotated, 2), round(y_rotated, 2))
