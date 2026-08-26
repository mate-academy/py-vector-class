from __future__ import annotations
import math


class Vector:

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple
                                    ) -> Vector:
        return cls(round((end_point[0] - start_point[0]), 2),
                   round((end_point[1] - start_point[1]), 2)
                   )

    def __init__(self, x_axis: float, y_axis: float) -> None:
        self.x = round(x_axis, 2)
        self.y = round(y_axis, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> int | float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(round(self.x * other, 2), round(self.y * other, 2))

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        magnitude = self.get_length()
        return Vector(round(self.x / magnitude, 2),
                      round(self.y / magnitude, 2)
                      )

    def angle_between(self, other: Vector) -> int:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        other = Vector(0, 1)
        return self.angle_between(other)

    def rotate(self, by_degrees: int) -> Vector:
        x_rotate = (self.x * math.cos(math.radians(by_degrees))
                    - self.y * math.sin(math.radians(by_degrees))
                    )
        y_rotate = (self.x * math.sin(math.radians(by_degrees))
                    + self.y * math.cos(math.radians(by_degrees))
                    )
        return Vector(x_rotate, y_rotate)
