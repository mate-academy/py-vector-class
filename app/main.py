from __future__ import annotations
import math


class Vector:
    def __init__(self, x_point: float, y_point: float) -> None:
        self.x = round(x_point, 2)
        self.y = round(y_point, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x_point=self.x + other.x,
            y_point=self.y + other.y,
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x_point=self.x - other.x,
            y_point=self.y - other.y,
        )

    def __mul__(self, other: int | float | Vector) -> Vector:
        if isinstance(other, Vector):
            return ((self.x * other.x)
                    + (self.y * other.y))
        return Vector(
            x_point=self.x * other,
            y_point=self.y * other
        )

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        cls.x = end_point[0] - start_point[0]
        cls.y = end_point[1] - start_point[1]
        return Vector(cls.x, cls.y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            x_point=self.x / self.get_length(),
            y_point=self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> int:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        length = self.get_length()
        cos_a = self.y / length
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_corner = math.cos(radians)
        sin_corner = math.sin(radians)
        return Vector(
            x_point=self.x * cos_corner - self.y * sin_corner,
            y_point=self.x * sin_corner + self.y * cos_corner
        )
