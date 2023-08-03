from __future__ import annotations
import math


class Vector:
    def __init__(self, point_x: int | float, point_y: int | float) -> None:
        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

    def __add__(self, other: float | int | Vector) -> Vector:
        if isinstance(other, Vector):
            vector_x = self.x + other.x
            vector_y = self.y + other.y
            return Vector(vector_x, vector_y)
        else:
            vector_x = self.x + other.x
            vector_y = self.y + other.y
            return Vector(vector_x, vector_y)

    def __sub__(self, other: float | int | Vector) -> Vector:
        if isinstance(other, Vector):
            vector_x = self.x - other.x
            vector_y = self.y - other.y
            return Vector(vector_x, vector_y)
        else:
            vector_x = self.x - other.x
            vector_y = self.y - other.y
            return Vector(vector_x, vector_y)

    def __mul__(self, other: float | int | Vector) -> Vector:
        if isinstance(other, Vector):
            dot_product = (self.x * other.x) + (self.y * other.y)
            return dot_product
        else:
            vector_x = self.x * other
            vector_y = self.y * other
        return Vector(vector_x, vector_y)

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: int | float, end_point: int | float
    ) -> Vector:
        vector_x = end_point[0] - start_point[0]
        vector_y = end_point[1] - start_point[1]
        return Vector(vector_x, vector_y)

    def get_length(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> float:
        dot_product = self * other
        gen_length = self.get_length() * other.get_length()
        cos_angle = dot_product / gen_length

        angle_radians = math.acos(cos_angle)
        angle_in_degrees = math.degrees(angle_radians)

        return round(angle_in_degrees)

    def get_angle(self) -> float:
        reference_vector = Vector(0, 1)
        angle_degrees = self.angle_between(reference_vector)
        return angle_degrees

    def rotate(self, degrees: float) -> Vector:
        angle_radians = math.radians(degrees)
        new_x = self.x * math.cos(angle_radians) - self.y * \
            math.sin(angle_radians)
        new_y = self.x * math.sin(angle_radians)\
            + self.y * math.cos(angle_radians)

        return Vector(new_x, new_y)
