from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            self.x = round(self.x * other, 2)
            self.y = round(self.y * other, 2)
            return self

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            round(end_point[0] - start_point[0], 2),
            round(end_point[1] - start_point[1], 2)
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            round(self.x / Vector.get_length(self), 2),
            round(self.y / Vector.get_length(self), 2)
        )

    def angle_between(self, other: Vector) -> int:
        cos_a = (
            (self * other)
            / (Vector.get_length(self) * Vector.get_length(other))
        )
        return round((math.degrees(math.acos(cos_a))))

    def get_angle(self) -> int:
        cos_a = self.y / Vector.get_length(self)
        return round((math.degrees(math.acos(cos_a))))

    def rotate(self, degrees: int) -> Vector:
        new_x = round(
            self.x * math.cos(math.radians(degrees))
            - self.y * math.sin(math.radians(degrees)),
            2
        )
        new_y = round(
            self.x * math.sin(math.radians(degrees))
            + self.y * math.cos(math.radians(degrees)),
            2
        )
        return Vector(new_x, new_y)
