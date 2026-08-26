from __future__ import annotations
import math


class Vector:
    def __init__(self, x_cord: int | float, y_cord: int | float) -> None:
        self.x = round(x_cord, 2)
        self.y = round(y_cord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(round(self.x + other.x, 2), round(self.y + other.y, 2))

    def __sub__(self, other: Vector) -> Vector:
        return Vector(round(self.x - other.x, 2), round(self.y - other.y, 2))

    def __mul__(self, other: int | Vector | float) -> Vector | int:
        if isinstance(other, (int, float)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, first: tuple, other: tuple) -> Vector:
        return Vector(round(other[0] - first[0], 2),
                      round(other[1] - first[1], 2))

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        return Vector(round(self.x / self.get_length(), 2),
                      round(self.y / self.get_length(), 2))

    def angle_between(self, other: Vector) -> int | float:
        dot_product = self.x * other.x + self.y * other.y
        cos_angle = dot_product / (self.get_length() * other.get_length())
        angle_in_radians = math.acos(cos_angle)
        angle_in_degrees = round(math.degrees(angle_in_radians))
        return angle_in_degrees

    def get_angle(self) -> int:
        reference_vector = Vector(0, 1)
        return self.angle_between(reference_vector)

    def rotate(self, degrees: int) -> Vector:
        radian = math.radians(degrees)
        new_x = round(self.x * math.cos(radian) - self.y * math.sin(radian), 2)
        new_y = round(self.x * math.sin(radian) + self.y * math.cos(radian), 2)
        return Vector(new_x, new_y)
