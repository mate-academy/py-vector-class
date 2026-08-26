from __future__ import annotations
import math


class Vector:
    def __init__(self, x_cor: float, y_cor: float) -> None:
        self.x = round(x_cor, 2)
        self.y = round(y_cor, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start: tuple[float | int, float | int],
            end: tuple[float | int, float | int]) -> Vector:
        return cls(end[0] - start[0], end[1] - start[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        return round(
            math.degrees(
                math.acos(max(
                    min(
                        (self.x * other.x + self.y * other.y)
                        / (

                            math.hypot(self.x, self.y)
                            * math.hypot(other.x, other.y)
                        )
                        , 1)
                    , -1)
                )
            )
        )

    def get_angle(self) -> float:
        return round(
            math.degrees(
                math.acos(max(min(self.y / math.hypot(self.x, self.y), 1), -1))
            )
        )

    def rotate(self, degrees: float) -> Vector:
        return Vector(
            round(self.x * math.cos(math.radians(degrees))
                  - self.y * math.sin(math.radians(degrees)), 2),
            round(self.x * math.sin(math.radians(degrees))
                  + self.y * math.cos(math.radians(degrees)), 2)
        )
