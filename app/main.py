from __future__ import annotations
import math


class Vector:
    def __init__(self, horizontal: float | int, vertical: float | int) -> None:
        self.x = round(horizontal, 2)
        self.y = round(vertical, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(horizontal=self.x + other.x,
                          vertical=self.y + other.y)
        return NotImplemented

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(horizontal=self.x - other.x,
                          vertical=self.y - other.y)
        return NotImplemented

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(horizontal=round(self.x * other, 2),
                          vertical=round(self.y * other, 2))
        if isinstance(other, Vector):
            return math.fabs(self.x * other.x) - math.fabs(self.y * other.y)
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        if isinstance((start_point, end_point), tuple):
            return cls(horizontal=round(end_point[0] - start_point[0], 2),
                       vertical=round(end_point[1] - start_point[1], 2))
        return NotImplemented

    def get_length(self) -> float:
        if isinstance(self, Vector):
            return math.sqrt(self.x**2 + self.y**2)
        return NotImplemented

    def get_normalized(self) -> Vector:
        if isinstance(self, Vector):
            return Vector(horizontal=round(self.x / self.get_length(), 2),
                          vertical=round(self.y / self.get_length(), 2))
        return NotImplemented

    def angle_between(self, other: Vector) -> int:
        if isinstance(other, Vector):
            dot_product = self.x * other.x + self.y * other.y
            lengths = self.get_length() * other.get_length()
            cos_theta = dot_product / lengths
            angle_rad = math.acos(cos_theta)
            angle_deg = math.degrees(angle_rad)
            return round(angle_deg)
        return NotImplemented

    def get_angle(self) -> int:
        length = math.hypot(self.x, self.y)
        cos_theta = self.y / length
        cos_theta = max(-1, min(1, cos_theta))
        angle = math.degrees(math.acos(cos_theta))
        return round(angle)

    def rotate(self, degrees: int) -> "Vector":
        if isinstance(degrees, int):
            theta = math.radians(degrees)

            new_x = self.x * math.cos(theta) - self.y * math.sin(theta)
            new_y = self.x * math.sin(theta) + self.y * math.cos(theta)

            return Vector(round(new_x, 2), round(new_y, 2))
        return NotImplemented
