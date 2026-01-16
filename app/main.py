from __future__ import annotations
import math


class Vector:

    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __repr__(self) -> str:
        return f"Vector {self.x, self.y}"

    def __add__(self, other: Vector) -> Vector:
        return (
            Vector(self.x + other.x, self.y + other.y)
            if isinstance(other, Vector) else None
        )

    def __sub__(self, other: Vector) -> Vector:
        return (
            Vector(self.x - other.x, self.y - other.y)
            if isinstance(other, Vector) else None
        )

    def __mul__(self, other: int | float | Vector) -> int | float | Vector:
        return (
            (self.x * other.x + self.y * other.y)
            if isinstance(other, Vector)
            else Vector(self.x * other, self.y * other)
        )

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple,
        end_point: tuple
    ) -> Vector:
        coord_x = (end_point[0] - start_point[0])
        coord_y = (end_point[1] - start_point[1])
        return cls(coord_x, coord_y)

    def get_length(self) -> int:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            round(self.x / self.get_length(), 2),
            round(self.y / self.get_length(), 2),
        )

    def angle_between(self, other: Vector) -> int:
        dot_prod = self * other
        len_self = self.get_length()
        len_other = other.get_length()

        cosine = dot_prod / (len_self * len_other)
        return round(math.degrees(math.acos(cosine)))

    def get_angle(self) -> int:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degrees: int | float) -> Vector:
        angle_radians = math.radians(degrees)
        new_x = (
            self.x * math.cos(angle_radians)
            - self.y * math.sin(angle_radians)
        )
        new_y = (
            self.x * math.sin(angle_radians)
            + self.y * math.cos(angle_radians)
        )
        return Vector(new_x, new_y)
