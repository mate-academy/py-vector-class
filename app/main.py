from __future__ import annotations

import math


class Vector:

    def __init__(self, axisx: float, axisy: float) -> None:
        self.x = round(axisx, 2)
        self.y = round(axisy, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(axisx=(self.x + other.x), axisy=(self.y + other.y))

    def __sub__(self, other: Vector) -> Vector:
        return Vector(axisx=(self.x - other.x), axisy=(self.y - other.y))

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, Vector):
            first = self.x * other.x
            second = self.y * other.y
            return first + second
        return Vector(axisx=round((self.x * other), 2),
                      axisy=round((self.y * other), 2))

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return Vector(
            axisx=end_point[0] - start_point[0],
            axisy=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(
            axisx=self.x / length,
            axisy=self.y / length
        )

    def angle_between(self, other: Vector) -> int:
        mul = self * other
        cos = mul / (self.get_length() * other.get_length())
        return round(math.acos(cos) * 57.2958)

    def get_angle(self) -> int:
        axis = Vector(0, 1)
        angle = self.angle_between(axis)
        return angle

    def rotate(self, degrees: int) -> Vector:

        radians = math.radians(degrees)
        return Vector(
            axisx=math.cos(radians) * self.x - math.sin(radians) * self.y,
            axisy=math.sin(radians) * self.x + math.cos(radians) * self.y
        )
