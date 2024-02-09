from __future__ import annotations
import math


class Vector:

    def __init__(self, x_vec: int | float, y_vec: int | float) -> None:
        if isinstance(x_vec, int):
            self.x = x_vec
        self.x = round(x_vec, 2)
        if isinstance(y_vec, int):
            self.y = y_vec
        self.y = round(y_vec, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x=self.x + other.x,
            y=self.y + other.y,
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x=self.x - other.x,
            y=self.y - other.y,
        )

    def __mul__(self, other: int | float | Vector) -> Vector:
        if isinstance(other, (int | float)):
            return Vector(
                x=self.x * other,
                y=self.y * other,
            )
        return (
            self.x * other.x + self.y * other.y
        )

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple) -> Vector:
        return cls(
            x=float(end_point[0]) - float(start_point[0]),
            y=float(end_point[1]) - float(start_point[1]),
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            round(self.x / self.get_length(), 2),
            round(self.y / self.get_length(), 2),
        )

    def angle_between(self, other: Vector) -> Vector:
        cos_a = (
            self * other
            / (self.get_length() * other.get_length())
        )

        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        angel = math.atan2(self.x, self.y)
        angel_to_degree = math.degrees(angel)
        return abs(round(angel_to_degree))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        x_2 = self.x * math.cos(radians) - self.y * math.sin(radians)
        y_2 = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(x_2, y_2)
