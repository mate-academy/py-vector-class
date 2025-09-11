from __future__ import annotations

import math


class Vector:
    def __init__(self, x_component: int | float,
                 y_component: int | float) -> None:
        self.x = round(x_component, 2)
        self.y = round(y_component, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(
                x_component=round((self.x + other.x), 2),
                y_component=round((self.y + other.y), 2)
            )

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(
                x_component=round((self.x - other.x), 2),
                y_component=round((self.y - other.y), 2)
            )

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        if isinstance(other, (int, float)):
            return Vector(
                x_component=round(self.x * other, 2),
                y_component=round(self.y * other, 2)
            )

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(
            x_component=round((end_point[0] - start_point[0]), 2),
            y_component=round((end_point[1] - start_point[1]), 2)
        )

    def get_length(self) -> float:
        return (self.x**2 + self.y**2)**0.5

    def get_normalized(self) -> Vector:
        return Vector(
            x_component=round((self.x / self.get_length()), 2),
            y_component=round((self.y / self.get_length()), 2)
        )

    def angle_between(self, other: Vector) -> float:
        return round(
            math.degrees(math.acos(
                (self.x * other.x + self.y * other.y)
                / (self.get_length() * other.get_length())
            )))

    def get_angle(self) -> float:
        return round(math.degrees(math.acos(self.y / self.get_length())))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
        return Vector(
            x_component=round(self.x * cos_theta - self.y * sin_theta, 2),
            y_component=round(self.x * sin_theta + self.y * cos_theta, 2)
        )
