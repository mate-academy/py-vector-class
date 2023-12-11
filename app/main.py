from __future__ import annotations
import math


class Vector:

    def __init__(self, point_x: int | float, point_y: int | float) -> None:
        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector((self.x + other.x), (self.y + other.y))

    def __sub__(self, other: Vector) -> Vector:
        return Vector((self.x - other.x), (self.y - other.y))

    def __mul__(self, other: int | float | Vector) -> int | float | Vector:
        if not isinstance(other, Vector):
            return Vector((self.x * other), (self.y * other))
        return (self.x * other.x) + (self.y * other.y)

    @staticmethod
    def create_vector_by_two_points(
        start_point: tuple, end_point: tuple
    ) -> Vector:
        return Vector(*end_point).__sub__(Vector(*start_point))

    def get_length(self) -> int | float:
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int | float:
        vector = self.__mul__(other)
        angle_rad = math.acos(vector / (
            self.get_length() * other.get_length())
        )
        angle_deg = math.degrees(angle_rad)
        return round(angle_deg)

    def get_angle(self) -> int | float:
        angle_rad = math.atan2(-self.x, self.y)
        result = (math.degrees(angle_rad) + 360) % 360
        return round(result)

    def rotate(self, degrees: int | float) -> Vector:
        angle_rad = math.radians(degrees)

        new_point_x = (
            self.x * math.cos(angle_rad) - self.y * math.sin(angle_rad)
        )
        new_point_y = (
            self.x * math.sin(angle_rad) + self.y * math.cos(angle_rad)
        )
        return Vector(new_point_x, new_point_y)
