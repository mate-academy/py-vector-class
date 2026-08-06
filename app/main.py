from __future__ import annotations
import math


class Vector:

    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x_coordinate=self.x + other.x,
            y_coordinate=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x_coordinate=self.x - other.x,
            y_coordinate=self.y - other.y
        )

    def __mul__(self, other: float | Vector) -> float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        if isinstance(other, float | int):
            return Vector(
                x_coordinate=round(self.x * other, 2),
                y_coordinate=round(self.y * other, 2)
            )

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple) -> Vector:
        return Vector(
            x_coordinate=end[0] - start[0],
            y_coordinate=end[1] - start[1]
        )

    def get_length(self) -> float:
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            x_coordinate=round(self.x / self.get_length(), 2),
            y_coordinate=round(self.y / self.get_length(), 2)
        )

    def angle_between(self, other: Vector) -> int:
        result = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(result)))

    def get_angle(self) -> int:
        result = (self * Vector(0, self.y)) / (self.get_length() * self.y)
        return round(math.degrees(math.acos(result)))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        x_2 = (math.cos(radians) * self.x) - (math.sin(radians) * self.y)
        y_2 = (math.sin(radians) * self.x) + (math.cos(radians) * self.y)
        return Vector(
            x_coordinate=round(x_2, 2),
            y_coordinate=round(y_2, 2)
        )
