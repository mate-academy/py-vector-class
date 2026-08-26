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

    def __mul__(self, other: int | float | Vector) -> float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return Vector(end_point[0], end_point[1]).__sub__(
            Vector(start_point[0], start_point[1]))

    def get_length(self) -> float:
        x_new = self.x ** 2
        y_new = self.y ** 2
        return math.sqrt(x_new + y_new)

    def get_normalized(self) -> Vector:
        magnitude = self.get_length()
        return Vector(self.x / magnitude, self.y / magnitude)

    def angle_between(self, other: Vector) -> int:
        dot_product = self.__mul__(other)
        magnitudes_product = self.get_length() * other.get_length()
        return round(math.degrees(math.acos(dot_product / magnitudes_product)))

    def get_angle(self) -> float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        degrees = math.radians(degrees)
        x_rotated = math.cos(degrees) * self.x - math.sin(degrees) * self.y
        y_rotated = math.sin(degrees) * self.x + math.cos(degrees) * self.y
        return Vector(x_rotated, y_rotated)
