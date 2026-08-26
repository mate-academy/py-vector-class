from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            comp_x = self.x + other.x
            comp_y = self.y + other.y
            return Vector(comp_x, comp_y)

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            comp_x = self.x - other.x
            comp_y = self.y - other.y
            return Vector(comp_x, comp_y)

    def __mul__(self, other: (Vector, int, float)) -> Vector | float:
        if isinstance(other, (int, float)):
            comp_x = self.x * other
            comp_y = self.y * other
            return Vector(comp_x, comp_y)
        elif isinstance(other, Vector):
            comp_x = self.x * other.x
            comp_y = self.y * other.y
            return comp_x + comp_y

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple) -> Vector:
        comp_x = end[0] - start[0]
        comp_y = end[1] - start[1]
        return cls(comp_x, comp_y)

    def get_length(self) -> (float, int):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        dot = self * other
        length_mul = self.get_length() * other.get_length()
        radian_angle = math.acos(dot / length_mul)
        return round(math.degrees(radian_angle))

    def get_angle(self) -> int:
        radian_angle = math.acos(self.y / self.get_length())
        return int(math.degrees(radian_angle))

    def rotate(self, angle: int) -> Vector:
        cos = math.cos(math.radians(angle))
        sin = math.sin(math.radians(angle))
        comp_x = self.x * cos - self.y * sin
        comp_y = self.x * sin + self.y * cos
        return Vector(comp_x, comp_y)
