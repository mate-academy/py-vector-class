from __future__ import annotations

import math


class Vector:
    def __init__(self, point_x: float | int, point_y: float | int) -> None:
        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            point_x=self.x + other.x,
            point_y=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            point_x=self.x - other.x,
            point_y=self.y - other.y
        )

    def __mul__(self, other: Vector | int | float) -> Vector | float | int:
        if isinstance(other, (int, float)):
            return Vector(
                point_x=self.x * other,
                point_y=self.y * other
            )
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(
            point_x=end_point[0] - start_point[0],
            point_y=end_point[1] - start_point[1]
        )

    def get_length(self) -> int | float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            point_x=self.x / self.get_length(),
            point_y=self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> float:
        skal = self.x * other.x + self.y * other.y
        a_sqrt = math.sqrt(self.x ** 2 + self.y ** 2)
        b_sqrt = math.sqrt(other.x ** 2 + other.y ** 2)
        return round(math.degrees(math.acos(skal / (a_sqrt * b_sqrt))))

    def get_angle(self) -> int:
        other = Vector(0, 1)
        skal = self.x * other.x + self.y * other.y
        a_sqrt = math.sqrt(self.x ** 2 + self.y ** 2)
        b_sqrt = math.sqrt(other.x ** 2 + other.y ** 2)
        return round(math.degrees(math.acos(skal / (a_sqrt * b_sqrt))))

    def rotate(self, degrees: int) -> Vector:
        cos = math.cos(math.radians(degrees))
        sin = math.sin(math.radians(degrees))
        x_cos = (cos * self.x) - (sin * self.y)
        y_sin = sin * self.x + cos * self.y
        return Vector(x_cos, y_sin)
