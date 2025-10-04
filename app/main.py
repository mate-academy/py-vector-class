from __future__ import annotations
import math
from math import degrees


class Vector:
    def __init__(self, x: int | float, y: int | float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector | None:
        if isinstance(other, Vector):
            return Vector((self.x + other.x), (self.y + other.y))

    def __sub__(self, other: Vector) -> Vector | None:
        if isinstance(other, Vector):
            return Vector((self.x - other.x), (self.y - other.y))

    def __mul__(self, other: int | float | Vector) -> float | None | Vector:
        if isinstance(other, (int, float)):
            return Vector((self.x * other), (self.y * other))
        if isinstance(other, Vector):
            dot_product = ((self.x * other.x) + (self.y * other.y))
            return dot_product
        return NotImplemented

    def __rmul__(self, other: int | float) -> None:
        return self.__mul__(other)

    @classmethod
    def create_vector(cls, start_point: tuple, end_point: tuple) -> Vector:
        dx = (end_point[0] - start_point[0])
        dy = (end_point[1] - start_point[1])
        return cls(dx, dy)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> None | int:
        dot_product = ((self.x * other.x) + (self.y * other.y))
        length_self = self.get_length()
        length_other = other.get_length()
        if length_self == 0 or length_other == 0:
            raise ValueError
        cos_angle = dot_product / (length_self * length_other)
        if cos_angle > 1:
            cos_angle = 1
        elif cos_angle < -1:
            cos_angle = -1
        return round(degrees(math.acos(cos_angle)))

    def get_angle(self) -> int:
        length = self.get_length()
        if length == 0:
            raise ValueError
        angle = self.y / length
        if angle > 1:
            angle = 1
        elif angle < -1:
            angle = -1
        return round(degrees(math.acos(angle)))

    def rotate(self, angle: int | float) -> Vector:
        rad = math.radians(angle)
        vect_x = (self.x * math.cos(rad)) - (self.y * math.sin(rad))
        vect_y = (self.x * math.sin(rad)) + (self.y * math.cos(rad))
        return Vector(vect_x, vect_y)
