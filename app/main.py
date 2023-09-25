from __future__ import annotations
import math


class Vector:  # chanched branche to develop
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)

    def __mul__(self, other: Vector | float) -> Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        x = round(self.x * other, 2)
        y = round(self.y * other, 2)
        return Vector(x, y)

    @staticmethod
    def create_vector_by_two_points(
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        x = (end_point[0] - start_point[0])
        y = (end_point[1] - start_point[1])
        return Vector(x, y)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        lenth_vector = self.get_length()
        x = round(self.x / lenth_vector, 2)
        y = round(self.y / lenth_vector, 2)
        return Vector(x, y)

    def angle_between(self, other: Vector) -> Vector:
        mul_lenth = Vector.get_length(self) * Vector.get_length(other)
        return round(math.degrees(math.acos(self * other / mul_lenth)))

    def get_angle(self) -> float:
        return Vector.angle_between(self, Vector(0, 1))

    def rotate(self, angle: int) -> Vector:
        angle = math.radians(angle)
        cos = math.cos(angle)
        sin = math.sin(angle)
        x = round(self.x * cos - self.y * sin, 2)
        y = round(self.x * sin + self.y * cos, 2)

        return Vector(x, y)
