from __future__ import annotations
import math
from math import sqrt


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __sub__(self, other: Vector) -> Vector:
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            new_s = self.x * other.x + self.y * other.y
            return new_s
        else:
            new_x = self.x * other
            new_y = self.y * other
            return Vector(new_x, new_y)

    @classmethod
    def create_vector_by_two_points(cls, start: tuple[float, float],
                                    end: tuple[float, float]) -> Vector:
        new_x = end[0] - start[0]
        new_y = end[1] - start[1]
        return cls(new_x, new_y)

    def get_length(self) -> float:
        length = sqrt(self.x ** 2 + self.y ** 2)
        return length

    def get_normalized(self) -> Vector:
        if self.get_length() != 0:
            length = self.get_length()
            new_x = self.x / length
            new_y = self.y / length
            return Vector(new_x, new_y)
        else:
            return Vector(0, 0)

    def angle_between(self, other: Vector) -> int:
        dot = self * other
        length_a = self.get_length()
        length_b = other.get_length()
        if length_a == 0 or length_b == 0:
            raise ValueError("Zero-length vector")
        else:
            cos_a = dot / (length_a * length_b)
            cos_a = max(-1.0, min(1.0, cos_a))
            angle = math.degrees(math.acos(cos_a))
            return round(angle)

    def get_angle(self) -> int:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degrees: float) -> Vector:
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
