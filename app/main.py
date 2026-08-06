from __future__ import annotations
import math


class Vector:

    def __init__(self, point_x: int, point_y: int) -> None:
        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

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

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, int | float):
            return Vector(
                round(self.x * other, 2),
                round(self.y * other, 2)
            )
        elif isinstance(other, Vector):
            return float(
                self.x * other.x + self.y * other.y
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

    def get_length(self) -> Vector:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> int:
        print(Vector.get_length(self))
        return round(math.degrees(
            math.acos(
                (self.x * other.x + self.y * other.y)
                / (Vector.get_length(self) * Vector.get_length(other))))
        )

    def get_angle(self) -> int:
        return round(math.degrees(
            math.acos(
                (self.x * 0 + self.y * abs(self.y))
                / (Vector.get_length(self) * ((0 + self.y ** 2) ** 0.5))))
        )

    def rotate(self, degree: int) -> Vector:
        converted_degree = math.radians(degree)
        return Vector(
            math.cos(converted_degree)
            * self.x - math.sin(converted_degree) * self.y,
            math.sin(converted_degree)
            * self.x + math.cos(converted_degree) * self.y
        )
