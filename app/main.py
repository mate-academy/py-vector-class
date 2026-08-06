from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: int | float, y_coord: int | float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, other: Vector | float | int) -> Vector | float | int:
        return (
            self.x * other.x + self.y * other.y
            if isinstance(other, Vector)
            else Vector(self.x * other, self.y * other)
        )

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

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length()
        )

    def angle_between(self, vector: Vector) -> int:
        return round(
            math.degrees(
                math.acos(
                    (self.x * vector.x + self.y * vector.y)
                    / (self.get_length() * vector.get_length())
                )
            )
        )

    def get_angle(self) -> int:
        return (
            int(360 - (math.degrees(math.atan2(self.x, self.y)) + 360) % 360)
            if (math.degrees(math.atan2(self.x, self.y)) + 360) % 360 != 0
            else 0
        )

    def rotate(self, degrees: int) -> Vector:
        return Vector(
            self.x * math.cos(math.radians(degrees))
            - self.y * math.sin(math.radians(degrees)),
            self.x * math.sin(math.radians(degrees))
            + self.y * math.cos(math.radians(degrees))
        )
