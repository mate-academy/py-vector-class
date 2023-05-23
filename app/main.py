from __future__ import annotations
import math


class Vector:
    def __init__(self, vector_x: float | int, vector_y: float | int) -> None:
        self.x = round(vector_x, 2)
        self.y = round(vector_y, 2)

    def __add__(self, other: Vector | float | int) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector | float | int) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float | int) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        start_x, start_y = start_point
        end_x, end_y = end_point
        return cls(end_x - start_x, end_y - start_y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int | float:
        return round(
            math.degrees(
                math.acos(
                    (self.x * other.x + self.y * other.y)
                    / (self.get_length() * other.get_length())
                )))

    def get_angle(self) -> Vector | int | float:
        return round(
            math.degrees(
                math.atan2(-self.x, self.y)) % 360)

    def rotate(self, other: Vector | int | float) -> Vector:
        radians = math.radians(other)
        angel_cos = math.cos(radians)
        angel_sin = math.sin(radians)
        rot_x = self.x * angel_cos - self.y * angel_sin
        rot_y = self.x * angel_sin + self.y * angel_cos
        return Vector(rot_x, rot_y)
