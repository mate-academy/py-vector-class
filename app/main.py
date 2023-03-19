from __future__ import annotations

import math


class Vector:
    def __init__(self, xx: int | float, yy: int | float) -> None:
        self.x = round(xx, 2)
        self.y = round(yy, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(xx=self.x + other.x, yy=self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(xx=self.x - other.x, yy=self.y - other.y)

    def __mul__(self, other: Vector | float | int) -> float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

    @staticmethod
    def create_vector_by_two_points(start_point: tuple,
                                    end_point: tuple) -> Vector:
        return Vector(xx=end_point[0] - start_point[0],
                      yy=end_point[1] - start_point[1]
                      )

    def get_length(self) -> int | float:
        return (self.x**2 + self.y**2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            xx=round(self.x / self.get_length(), 2),
            yy=round(self.y / self.get_length(), 2),
        )

    def angle_between(self, other: Vector) -> int | float:
        dot_product = self.x * other.x + self.y * other.y
        get_magnitude = self.get_length() * other.get_length()
        angle = math.acos(dot_product / get_magnitude)
        return round(math.degrees(angle))

    def get_angle(self) -> int | float:
        return round(math.degrees(math.atan2(-self.x, self.y)) % 360)

    def rotate(self, degrees: int) -> Vector:
        rad = math.radians(degrees)
        new_x = self.x * math.cos(rad) - self.y * math.sin(rad)
        new_y = self.x * math.sin(rad) + self.y * math.cos(rad)
        return Vector(new_x, new_y)
