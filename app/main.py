from __future__ import annotations
import math


class Vector:
    def __init__(self, x_point: float, y_point: float) -> None:
        self.x = round(x_point, 2)
        self.y = round(y_point, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.x + other.x,
            self.y + other.y,
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x - other.x,
            self.y - other.y,
        )

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(
            self.x * other,
            self.y * other,
        )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1],
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> float:
        return Vector(
            round(self.x / self.get_length(), 2),
            round(self.y / self.get_length(), 2),
        )

    def angle_between(self, other: Vector) -> int:
        return round(
            math.degrees(
                math.acos(
                    self.__mul__(other)
                    / (other.get_length() * self.get_length())
                )
            )
        )

    def get_angle(self) -> int:
        result = abs(round(math.degrees(math.atan(self.x / self.y))))
        if self.x < 0 and self.y < 0:
            return 180 - result
        return result

    def rotate(self, degrees: int) -> Vector:
        return Vector(
            math.cos(math.radians(degrees)) * self.x
            - math.sin(math.radians(degrees)) * self.y,
            math.sin(math.radians(degrees)) * self.x
            + math.cos(math.radians(degrees)) * self.y,
        )
