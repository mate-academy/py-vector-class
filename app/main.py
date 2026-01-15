from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coordinate: int | float,
                 y_coordinate: int | float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: int | float) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: int | float) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float) -> float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls((end_point[0] - start_point[0]),
                   (end_point[1] - start_point[1]))

    def get_length(self) -> int | float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        else:
            normalized_x = self.x / length
            normalized_y = self.y / length
            return Vector(normalized_x, normalized_y)

    def angle_between(self, other: Vector) -> int:
        dot_product = self.x * other.x + self.y * other.y
        vector1_length = self.get_length()
        vector2_length = other.get_length()
        cos_angle = dot_product / (vector1_length * vector2_length)
        angle_in_radians = math.acos(cos_angle)
        angle_in_degrees = math.degrees(angle_in_radians)
        return round(angle_in_degrees)

    def get_angle(self) -> int | float:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degrees: int) -> Vector:
        degrees = math.radians(degrees)
        rotated_x = math.cos(degrees) * self.x - math.sin(degrees) * self.y
        rotated_y = math.cos(degrees) * self.y + math.sin(degrees) * self.x
        return Vector(rotated_x, rotated_y)
