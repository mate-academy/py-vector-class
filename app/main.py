from __future__ import annotations
import math


class Vector:
    def __init__(self, point_x: float, point_y: float) -> None:
        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return Vector(
            end_point[0] - start_point[0], end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        dot = (self.x * other.x + self.y * other.y)
        cos_theta = dot / (self.get_length() * other.get_length())
        angle_rad = math.acos(cos_theta)
        return round(math.degrees(angle_rad))

    def get_angle(self) -> int:
        cos_theta = self.y / self.get_length()
        angle_rad = math.acos(cos_theta)
        return round(math.degrees(angle_rad))

    def rotate(self, degrees: int) -> Vector:
        angle_radian = math.radians(degrees)
        cos = math.cos(angle_radian)
        sin = math.sin(angle_radian)
        return Vector(self.x * cos - self.y * sin, self.x * sin + self.y * cos)
