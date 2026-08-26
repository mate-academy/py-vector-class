from __future__ import annotations

import math


class Vector:
    def __init__(self, x_axile: float, y_axile: float) -> None:
        self.x = round(x_axile, 2)
        self.y = round(y_axile, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):  # скалярний добуток - dot product
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0], end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        return math.ceil(
            math.degrees(
                math.acos(
                    (self * other) / (self.get_length() * other.get_length())
                )
            )
        )

    def get_angle(self) -> int:
        return int(abs(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, degree: int) -> Vector:
        return Vector(
            self.x * math.cos(math.radians(degree))
            - self.y * math.sin(math.radians(degree)),
            self.x * math.sin(math.radians(degree))
            + self.y * math.cos(math.radians(degree)),
        )
