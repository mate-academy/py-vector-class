from __future__ import annotations
import math


class Vector:
    def __init__(self, coordinate_x: float, coordinate_y: float) -> None:
        self.x = round(coordinate_x, 2)
        self.y = round(coordinate_y, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, int | float):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @staticmethod
    def create_vector_by_two_points(
            start_point: tuple, end_point: tuple
    ) -> Vector:
        point_x = end_point[0] - start_point[0]
        point_y = end_point[1] - start_point[1]
        return Vector(point_x, point_y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        point_x = self.x / self.get_length()
        point_y = self.y / self.get_length()
        return Vector(point_x, point_y)

    def angle_between(self, vector: Vector) -> int:
        cos_a = self * vector / (self.get_length() * vector.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        vector = Vector(0, 1)
        return self.angle_between(vector)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        point_x = math.cos(radians) * self.x - math.sin(radians) * self.y
        point_y = math.sin(radians) * self.x + math.cos(radians) * self.y
        return Vector(point_x, point_y)
