from __future__ import annotations
import math


class Vector:
    def __init__(self, dot_x: float, dot_y: float) -> None:
        self.x = round(dot_x, 2)
        self.y = round(dot_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float) -> Vector | int | float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple[float, float],
            end_point: tuple[float, float]) -> Vector:
        point_x = round(end_point[0] - start_point[0], 2)
        point_y = round(end_point[1] - start_point[1], 2)
        return cls(point_x, point_y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector | int | float) -> float:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        cos_a = self.y / self.get_length()
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: float) -> Vector:
        radians = math.radians(degrees)
        point_x = \
            self.x * math.cos(radians) - self.y * math.sin(radians)
        point_y = \
            self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(point_x, point_y)
