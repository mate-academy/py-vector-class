from __future__ import annotations
import math


class Vector:
    def __init__(self, point_x: int | float, point_y: int | float) -> None:
        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float | int) -> Vector | int:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        sub_points1 = end_point[0] - start_point[0]
        sub_points2 = end_point[1] - start_point[1]
        return cls(sub_points1, sub_points2)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length_self = self.get_length()
        if length_self == 0:
            raise ValueError("length is zero")
        return Vector(self.x / length_self, self.y / length_self)

    def angle_between(self, other: Vector) -> float:
        dot_prod = self * other
        cos_angle = float(dot_prod) / (self.get_length() * other.get_length())
        angle_radius = math.acos(cos_angle)
        angle_degrees = math.degrees(angle_radius)
        return round(angle_degrees)

    def get_angle(self) -> int:
        angle_radians = math.atan2(self.x, self.y)
        angle_degrees = math.degrees(angle_radians)
        return abs(round(angle_degrees))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_angle = math.cos(radians)
        sin_angle = math.sin(radians)
        rotated_x = self.x * cos_angle - self.y * sin_angle
        rotated_y = self.x * sin_angle + self.y * cos_angle
        return Vector(rotated_x, rotated_y)
