from __future__ import annotations
from math import sqrt, degrees, acos, radians, cos, sin


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

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if not isinstance(other, Vector):
            return Vector(
                self.x * other,
                self.y * other
            )

        return self.get_dot_product(other)

    def get_dot_product(self, other: Vector) -> int | float:
        return self.x * other.x + self.y * other.y

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

    def get_length(self) -> int | float:
        return self.get_len_static(self)

    @staticmethod
    def get_len_static(vector: Vector) -> int | float:
        return sqrt(vector.x ** 2 + vector.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> int | float:
        return round(
            degrees(
                acos(
                    self.get_dot_product(other)
                    / (self.get_len_static(self) * self.get_len_static(other))
                )
            )
        )

    def get_angle(self) -> int | float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degs: int | float) -> Vector:
        rads = radians(degs)

        return Vector(
            (cos(rads) * self.x - sin(rads) * self.y),
            (sin(rads) * self.x + cos(rads) * self.y)
        )
