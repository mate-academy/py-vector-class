from __future__ import annotations

import math


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, int | float):
            return Vector(
                self.x * other,
                self.y * other
            )
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        x_coordinate = end_point[0] - start_point[0]
        y_coordinate = end_point[1] - start_point[1]
        return Vector(x_coordinate, y_coordinate)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> float:
        return round(
            math.degrees(
                math.acos(
                    (self * other) / (self.get_length() * other.get_length())
                )
            ), 0
        )

    def get_angle(self) -> float:
        vector2 = Vector(0, 1)
        return self.angle_between(vector2)

    def rotate(self, degrees: int) -> Vector:
        angle_rad = math.radians(degrees)
        x_new = self.x * math.cos(angle_rad) - self.y * math.sin(angle_rad)
        y_new = self.x * math.sin(angle_rad) + self.y * math.cos(angle_rad)
        return Vector(x_new, y_new)
