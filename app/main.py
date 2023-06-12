from __future__ import annotations

import math


class Vector:
    def __init__(self,
                 x_component: int | float,
                 y_component: int | float
                 ) -> None:
        self.x = round(x_component, 2)
        self.y = round(y_component, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(x_component=self.x + other.x,
                      y_component=self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(x_component=self.x - other.x,
                      y_component=self.y - other.y)

    def __mul__(self, other: Vector | float | int) -> Vector | float | int:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(x_component=self.x * other,
                      y_component=self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple
                                    ) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float | int:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(),
                      self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        rad = math.radians(degrees)
        x_rotate = math.cos(rad) * self.x - math.sin(rad) * self.y
        y_rotate = math.sin(rad) * self.x + math.cos(rad) * self.y
        return Vector(x_rotate, y_rotate)
