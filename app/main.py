from __future__ import annotations
import math


class Vector:
    def __init__(self, coor_x: float, coor_y: float) -> None:
        self.x = round(coor_x, 2)
        self.y = round(coor_y, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple)\
            -> Vector:
        coor_x = end_point[0] - start_point[0]
        coor_y = end_point[1] - start_point[1]
        return cls(coor_x, coor_y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> float:
        dot_product = self * other
        length_self = self.get_length()
        length_other = other.get_length()
        if length_self == 0 or length_other == 0:
            raise ValueError("You cannot divide by zero")
        cos = dot_product / (length_self * length_other)
        angle_in_rad = math.acos(cos)
        angle_in_degrees = math.degrees(angle_in_rad)
        return round(angle_in_degrees)

    def get_angle(self) -> float:
        vertical_vector = Vector(0, 1)
        return self.angle_between(vertical_vector)

    def rotate(self, degrees: float) -> Vector:
        radians = math.radians(degrees)
        x_new = self.x * math.cos(radians) - self.y * math.sin(radians)
        y_new = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(round(x_new, 2), round(y_new, 2))
