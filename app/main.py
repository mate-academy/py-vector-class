from __future__ import annotations
import math


class Vector:

    def __init__(self, point_x: float, point_y: float) -> None:
        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(
                self.x + other.x, self.y + other.y
            )
        return NotImplemented

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(
                self.x - other.x, self.y - other.y
            )
        return NotImplemented

    def __mul__(self, other: Vector | float | int) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        if isinstance((start_point, end_point), tuple):
            return cls(
                end_point[0] - start_point[0], end_point[1] - start_point[1]
            )
        return NotImplemented

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        len_vector = self.get_length()
        return Vector(self.x / len_vector, self.y / len_vector)

    def angle_between(self, other: Vector) -> int:
        if isinstance(other, Vector):
            angle_rad = math.acos(
                (self * other) / (self.get_length() * other.get_length())
            )
            angle_deg = math.degrees(angle_rad)
            return round(angle_deg, 0)
        return NotImplemented

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, angle_deg: int) -> Vector:
        if isinstance(angle_deg, int):
            rad = math.radians(angle_deg)  # перевод в радианы
            return Vector(
                self.x * math.cos(rad) - self.y * math.sin(rad),
                self.x * math.sin(rad) + self.y * math.cos(rad)
            )
        return NotImplemented
