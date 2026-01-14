from __future__ import annotations
import math


class Vector:

    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        x_coordinate = self.x + other.x
        y_coordinate = self.y + other.y
        return Vector(x_coordinate, y_coordinate)

    def __sub__(self, other: Vector) -> Vector:
        x_coordinate = self.x - other.x
        y_coordinate = self.y - other.y
        return Vector(x_coordinate, y_coordinate)

    def __mul__(self, other: float | Vector) -> Vector | float:
        if isinstance(other, Vector):
            x_coordinate = self.x * other.x
            y_coordinate = self.y * other.y
            return x_coordinate + y_coordinate
        x_coordinate = round(self.x * other, 2)
        y_coordinate = round(self.y * other, 2)
        return Vector(x_coordinate, y_coordinate)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start: tuple,
            end: tuple
    ) -> Vector:
        x_coordinate = end[0] - start[0]
        y_coordinate = end[1] - start[1]
        return cls(x_coordinate, y_coordinate)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length != 0:
            return Vector(
                self.x / length,
                self.y / length)
        return Vector(0, 0)

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        cos_angle = dot_product / (self.get_length() * other.get_length())
        angle_radians = math.acos(cos_angle)
        angle_degrees = math.degrees(angle_radians)
        return round(angle_degrees)

    def get_angle(self) -> int:
        y_coordinate_vector = Vector(0, 1)
        angle_degrees = self.angle_between(y_coordinate_vector)
        return angle_degrees

    def rotate(self, degrees: int) -> Vector:
        angle_radians = math.radians(degrees)
        x_mul_cos = self.x * math.cos(angle_radians)
        y_mul_sin = self.y * math.sin(angle_radians)
        new_x_coordinate = x_mul_cos - y_mul_sin

        x_mul_sin = self.x * math.sin(angle_radians)
        y_mul_cos = self.y * math.cos(angle_radians)
        new_y_coordinate = x_mul_sin + y_mul_cos

        return Vector(new_x_coordinate, new_y_coordinate)
