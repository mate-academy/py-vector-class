from __future__ import annotations
import math


class Vector:
    def __init__(self, x_value: [int, float], y_value: [int, float]) -> None:
        self.x = round(x_value, 2)
        self.y = round(y_value, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x_value=self.x + other.x,
            y_value=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x_value=self.x - other.x,
            y_value=self.y - other.y
        )

    def __mul__(self, other: [int, float, Vector]) -> [Vector, float, int]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(
            x_value=round(self.x * other, 2),
            y_value=round(self.y * other, 2)
        )

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(
            x_value=end_point[0] - start_point[0],
            y_value=end_point[1] - start_point[1]
        )

    def get_length(self) -> [int, float]:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(
            x_value=self.x / length,
            y_value=self.y / length
        )

    def angle_between(self, other: Vector) -> [int, float]:
        return round((math.degrees(math.acos(
            (self.x * other.x + self.y * other.y)
            / (self.get_length() * other.get_length())))), 0)

    def get_angle(self) -> [int, float]:
        return round((math.degrees(math.acos(self.y / self.get_length()))), 0)

    def rotate(self, degrees: int) -> Vector:
        return Vector(
            x_value=math.cos(
                math.radians(degrees)) * self.x - math.sin(
                math.radians(degrees)) * self.y,
            y_value=math.sin(
                math.radians(degrees)) * self.x + math.cos(
                math.radians(degrees)) * self.y
        )
