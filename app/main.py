from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float | Vector) -> float | Vector:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple) -> Vector:
        res_x = end[0] - start[0]
        res_y = end[1] - start[1]
        return cls(res_x, res_y)

    def get_length(self) -> float:
        return (self.x**2 + self.y**2)**0.5

    def get_normalized(self) -> Vector:
        magnitude = self.get_length()
        return Vector(self.x / magnitude, self.y / magnitude)

    def angle_between(self, other: Vector) -> float:
        dot_product = self * other
        self_magnitude = self.get_length()
        other_magnitude = other.get_length()
        cos_a = dot_product / (self_magnitude * other_magnitude)
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degrees: int) -> Vector:
        degrees = math.radians(degrees)
        res_x = math.cos(degrees) * self.x - math.sin(degrees) * self.y
        res_y = math.sin(degrees) * self.x + math.cos(degrees) * self.y
        return Vector(res_x, res_y)
