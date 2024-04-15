from __future__ import annotations
import math


class Vector:
    def __init__(self, x_: float | int, y_: float | int) -> None:
        self.x = round(x_, 2)
        self.y = round(y_, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x_=self.x + other.x,
            y_=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x_=self.x - other.x,
            y_=self.y - other.y
        )

    def __mul__(self, other: int | float | Vector) -> float | Vector:
        if isinstance(other, (int, float)):
            return Vector(
                x_=self.x * other,
                y_=self.y * other
            )
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_points: tuple,
                                    end_point: tuple) -> Vector:
        return Vector(
            x_=end_point[0] - start_points[0],
            y_=end_point[1] - start_points[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            x_=self.x / Vector.get_length(self),
            y_=self.y / Vector.get_length(self)
        )

    def angle_between(self, other: Vector) -> int:
        angle = math.degrees(math.acos(
            Vector.__mul__(self, other)
            / (Vector.get_length(self) * Vector.get_length(other))
        ))
        return round(angle)

    def get_angle(self) -> int:
        return round(math.degrees(
            math.acos(self.y / Vector.get_length(self))
        ))

    def rotate(self, degrees: int) -> Vector:
        return Vector(
            x_=self.x * math.cos(math.radians(degrees))
            - self.y * math.sin(math.radians(degrees)),
            y_=self.x * math.sin(math.radians(degrees))
            + self.y * math.cos(math.radians(degrees))
        )
