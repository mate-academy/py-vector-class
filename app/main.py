from __future__ import annotations
import math


class Vector:
    def __init__(self, x: int | float, y: int | float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float | int) -> Vector | int | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0], end_point[1] - start_point[1]
        )

    def get_length(self) -> float | int:
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> Vector | int | float:
        return round(math.degrees(math.acos(
            ((self.x * other.x) + (self.y * other.y))/(
                (math.sqrt((self.x ** 2) + (self.y ** 2))) * (
                    math.sqrt((other.x ** 2) + (other.y ** 2)))
            )
        )))

    def get_angle(self) -> int | float:
        positive_y_axis = Vector(0, 1)
        return self.angle_between(positive_y_axis)

    def rotate(self, degrees: int | float) -> Vector:
        radians = math.radians(degrees)
        c, s = math.cos(radians), math.sin(radians)
        return Vector(
            self.x * c - self.y * s, self.x * s + self.y * c
        )
