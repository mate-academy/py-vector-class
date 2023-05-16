from __future__ import annotations
import math


class Vector:

    def __init__(self, iks: int | float, igrek: int | float) -> None:
        self.x = round(iks, 2)
        self.y = round(igrek, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | Vector) -> Vector | int | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start: tuple,
            end: tuple) -> Vector:
        return cls(end[0] - start[0], end[1] - start[1])

    def get_length(self) -> float | int:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        x_res = round(self.x / self.get_length(), 2)
        y_res = round(self.y / self.get_length(), 2)
        return Vector(x_res, y_res)

    def angle_between(self, vector: Vector) -> int:
        len_self = self.get_length()
        len_vec = vector.get_length()
        cos_a = (self * vector) / (len_self * len_vec)
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        sin_a = self.y / self.get_length()
        return round(math.degrees(math.acos(sin_a)))

    def rotate(self, degrees: int) -> Vector:
        angle = degrees
        sin_beta = math.sin(math.radians(angle))
        cos_beta = math.cos(math.radians(angle))
        r_minus_u = self.x * cos_beta - self.y * sin_beta
        t_plus_s = self.x * sin_beta + self.y * cos_beta
        return Vector(r_minus_u, t_plus_s)
