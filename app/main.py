from __future__ import annotations
import math
from math import sqrt


class Vector:
    def __init__(self, _x: float, _y: float) -> None:
        self.x = round(_x, 2)
        self.y = round(_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float | Vector) -> Vector | float:
        if isinstance(other, float | int):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        else:
            return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> float:
        dot_product = self.x * other.x + self.y * other.y
        self_length = self.get_length()
        other_length = other.get_length()

        if self_length == 0 or other_length == 0:
            return 0

        cosine_theta = dot_product / (self_length * other_length)
        theta_radians = math.acos(
            max(-1, min(1, cosine_theta)))
        theta_degrees = math.degrees(theta_radians)
        return round(theta_degrees)

    def get_angle(self) -> int:
        print(math.degrees(math.atan2(self.x, self.y)))
        return abs(round(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
