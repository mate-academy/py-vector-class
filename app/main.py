from __future__ import annotations
import math


class Vector:
    def __init__(self, x: int or float, y: int or float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x=self.x + other.x,
            y=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x=self.x - other.x,
            y=self.y - other.y
        )

    def __mul__(self, other: int or float or Vector) -> Vector:
        if isinstance(other, (int, float)):
            return Vector(
                x=self.x * other,
                y=self.y * other
            )

        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(
            x=end_point[0] - start_point[0],
            y=end_point[1] - start_point[1]
        )

    def get_length(self) -> int or float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            x=self.x / self.get_length(),
            y=self.y / self.get_length()
        )

    def angle_between(self, vector: Vector) -> int or float:
        return round(math.degrees(
            math.acos(
                Vector.__mul__(self, vector)
                / (self.get_length() * vector.get_length()))))

    def get_angle(self) -> int or float:
        return math.fabs(round(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, degrees: int or float) -> Vector:
        return Vector(
            x=(
                self.x * math.cos(math.radians(degrees))
                - self.y * math.sin(math.radians(degrees))
            ),
            y=(self.x * math.sin(math.radians(degrees))
                    + self.y * math.cos(math.radians(degrees))
            )
        )
