from __future__ import annotations

import math


class Vector:
    def __init__(self, x_pos: float, y_pos: float) -> None:
        self.x = round(x_pos, 2)
        self.y = round(y_pos, 2)

    def __add__(self, other: Vector) -> Vector | None:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError(f"unsupported type of {other} for +")

    def __sub__(self, other: Vector) -> Vector | None:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        else:
            raise TypeError(f"unsupported type of {other} for -")

    def __mul__(self, other: Vector | float | int) -> Vector | float | None:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, float | int):
            return Vector(self.x * other, self.y * other)
        else:
            raise TypeError(f"unsupported type of {other} for *")

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1]
                   )

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        return round(
            math.degrees(
                math.acos(
                    (self * other) / (self.get_length() * other.get_length()))
            )
        )

    def get_angle(self) -> int:
        return round(math.degrees(
            math.acos((self * Vector(0, 1)) / self.get_length())
        ))

    def rotate(self, degrees: int) -> Vector:
        return Vector(
            (
                (math.cos(math.radians(degrees)) * self.x)
                - math.sin(math.radians(degrees)) * self.y
            ),
            (math.sin(math.radians(degrees)) * self.x)
            + (math.cos(math.radians(degrees)) * self.y),
        )
