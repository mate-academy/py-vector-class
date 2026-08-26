from __future__ import annotations
import math


class Vector:
    def __init__(self, x_axis: int | float, y_axis: int | float) -> None:
        self.x = round(x_axis, 2)
        self.y = round(y_axis, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, multiplier: Vector | int | float) -> Vector | int:
        if isinstance(multiplier, Vector):
            return self.x * multiplier.x + self.y * multiplier.y
        return Vector(self.x * multiplier, self.y * multiplier)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float | int:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        return round(
            math.degrees(
                math.acos(
                    (self * other) / (self.get_length() * other.get_length())
                )
            )
        )

    def get_angle(self) -> int:
        return round(
            math.degrees(
                math.acos(self.y / self.get_length())
            )
        )

    def rotate(self, angle: int) -> Vector:
        rad = math.radians(angle)
        return Vector(
            math.cos(rad) * self.x - math.sin(rad) * self.y,
            math.sin(rad) * self.x + math.cos(rad) * self.y
        )
