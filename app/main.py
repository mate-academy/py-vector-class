from __future__ import annotations

import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x_coord=self.x + other.x,
            y_coord=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x_coord=self.x - other.x,
            y_coord=self.y - other.y
        )

    def __mul__(self, other: Vector | float) -> Vector | float:
        if not isinstance(other, Vector):
            return Vector(
                x_coord=self.x * other,
                y_coord=self.y * other
            )
        return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(
            x_coord=(start_point[0] - end_point[0]) * -1,
            y_coord=(start_point[1] - end_point[1]) * -1
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** .5

    def get_normalized(self) -> Vector:
        return Vector(
            x_coord=round(self.x / self.get_length(), 2),
            y_coord=round(self.y / self.get_length(), 2)
        )

    def angle_between(self, other: Vector) -> int:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        theta = math.radians(degrees)
        new_x = (math.cos(theta) * self.x
                 - math.sin(theta) * self.y)
        new_y = (math.sin(theta) * self.x
                 + math.cos(theta) * self.y)
        return Vector(x_coord=new_x, y_coord=new_y)
