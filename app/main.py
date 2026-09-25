from __future__ import annotations
from math import sqrt
import math


class Vector:
    def __init__(self, cord_x: float, cord_y: float) -> None:
        self.x = round(cord_x, 2)
        self.y = round(cord_y, 2)

    def __add__(self, other : Vector) -> Vector:
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(round(new_x, 2), round(new_y, 2))

    def __sub__(self, other : Vector) -> Vector:
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(round(new_x, 2), round(new_y, 2))

    def __mul__(self, other: Vector | int) -> Vector:
        if isinstance(other, Vector):
            new_x = (self.x * other.x) + (self.y * other.y)
            return new_x
        else:
            new_x = self.x * other
            new_y = self.y * other
            return Vector(new_x, new_y)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point : tuple, end_point : tuple
    ) -> Vector :
        new_x = end_point[0] - start_point[0]
        new_y = end_point[1] - start_point[1]
        return cls(round(new_x, 2), round(new_y, 2))

    def get_length(self) -> float :
        new_x = sqrt((self.x ** 2) + (self.y ** 2))
        return new_x

    def get_normalized(self) -> Vector :
        new_x = self.x / self.get_length()
        new_y = self.y / self.get_length()
        return Vector(round(new_x, 2), round(new_y, 2))

    def angle_between(self, other : Vector) -> int :
        new_x = (self.x * other.x) + (self.y * other.y)
        new_y = self.get_length() * other.get_length()
        cos_a = new_x / new_y
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int :
        angel = Vector(0, 1)
        return round(self.angle_between(angel))

    def rotate(self, degrees : int) -> Vector :
        coso = math.cos(math.radians(degrees))
        sino = math.sin(math.radians(degrees))
        new_x = self.x * coso - self.y * sino
        new_y = self.x * sino + self.y * coso
        return Vector(round(new_x, 2), round(new_y, 2))
