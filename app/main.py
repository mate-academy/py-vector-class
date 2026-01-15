from __future__ import annotations
import math


class Vector:
    def __init__(self, os_x: int | float, os_y: int | float) -> Vector:
        self.x = round(os_x, 2)
        self.y = round(os_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | Vector) -> int | Vector:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector(round(self.x * other, 2),
                      round(self.y * other, 2))

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls((end_point[0] - start_point[0]),
                   (end_point[1] - start_point[1]))

    def get_length(self) -> float:
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def get_normalized(self) -> Vector:
        self_lenght = math.sqrt((self.x ** 2) + (self.y ** 2))
        norm_x = self.x / self_lenght
        norm_y = self.y / self_lenght
        return Vector(norm_x, norm_y)

    def angle_between(self, other: Vector) -> int:
        scalar_mult = self.x * other.x + self.y * other.y
        cos_angle = scalar_mult / (self.get_length() * other.get_length())
        angle_rad = math.acos(cos_angle)
        return round(angle_rad * 180 / math.pi, 0)

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, rotate_angle: int) -> Vector:
        rotate_radians = math.radians(rotate_angle)
        rotate_x = round(self.x * math.cos(rotate_radians)
                         - self.y * math.sin(rotate_radians), 2)
        rotate_y = round(self.y * math.cos(rotate_radians)
                         + self.x * math.sin(rotate_radians), 2)
        return Vector(rotate_x, rotate_y)
