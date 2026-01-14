from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        return (
            self.x * other.x + self.y * other.y
            if isinstance(other, Vector)
            else Vector(self.x * other, self.y * other)
        )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[float, float],
            end_point: tuple[float, float]
    ) -> Vector:
        return Vector(*end_point) - Vector(*start_point)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        vector_length = self.get_length()
        return Vector(self.x / vector_length, self.y / vector_length)

    def angle_between(self, other: Vector) -> int:
        return round(math.degrees(math.acos(
            (self * other) / (self.get_length() * other.get_length())
        )))

    def get_angle(self) -> int:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degrees: int) -> Vector:
        angle_in_rad = math.radians(degrees)
        x2 = self.x * math.cos(angle_in_rad) - self.y * math.sin(angle_in_rad)
        y2 = self.x * math.sin(angle_in_rad) + self.y * math.cos(angle_in_rad)
        return Vector(x2, y2)
