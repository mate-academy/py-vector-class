from __future__ import annotations
from math import sqrt, degrees, acos, cos, sin, radians


class Vector:

    def __init__(self, point_x: float, point_y: float) -> None:
        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector((self.x + other.x), (self.y + other.y))

    def __sub__(self, other: Vector) -> Vector:
        return Vector((self.x - other.x), (self.y - other.y))

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        else:
            return Vector((self.x * other), (self.y * other))

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple[float, float],
            end_point: tuple[float, float]
    ) -> Vector:
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1])

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(degrees(acos(cos_a)))

    def get_angle(self) -> int:
        vector_y = Vector(0, 1)
        return self.angle_between(vector_y)

    def rotate(self, angle: float) -> Vector:
        angle = radians(angle)
        return Vector(self.x * cos(angle) - self.y * sin(angle),
                      self.y * cos(angle) + self.x * sin(angle))
