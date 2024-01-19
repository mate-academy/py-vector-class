from __future__ import annotations

import math


class Vector:
    def __init__(self, x_value: float, y_value: float) -> None:
        self.x = round(x_value, 2)
        self.y = round(y_value, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(x_value=round(self.x + other.x, 2),
                      y_value=round(self.y + other.y, 2))

    def __sub__(self, other: Vector) -> Vector:
        return Vector(x_value=round(self.x - other.x, 2),
                      y_value=round(self.y - other.y, 2))

    def __mul__(self, other: Vector | float) -> Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(x_value=round(self.x * other, 2),
                          y_value=round(self.y * other, 2))

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(
            x_value=end_point[0] - start_point[0],
            y_value=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(x_value=round(self.x / self.get_length(), 2),
                      y_value=round(self.y / self.get_length(), 2))

    def angle_between(self, other: Vector) -> float:
        return round(
            math.degrees(
                math.acos(
                    (self.x * other.x + self.y * other.y)
                    / (self.get_length() * other.get_length()
                       )
                )
            ))

    def get_angle(self) -> float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, angle: int) -> Vector:
        return Vector(
            x_value=round(self.x * math.cos(math.radians(angle))
                          - self.y * math.sin(math.radians(angle)), 2),
            y_value=round(self.x * math.sin(math.radians(angle))
                          + self.y * math.cos(math.radians(angle)), 2)
        )
