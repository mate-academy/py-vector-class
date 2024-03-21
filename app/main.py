from __future__ import annotations
import math


class Vector:
    def __init__(self, x_arg: float, y_arg: float) -> None:
        self.x = round(x_arg, 2)
        self.y = round(y_arg, 2)

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

    def __mul__(self, other: Vector | float) -> float | Vector:
        if isinstance(other, Vector):
            dot_product = (self.x * other.x) + (self.y * other.y)
            return dot_product
        return Vector(
            self.x * other.real,
            self.y * other.real
        )

    @classmethod
    def create_vector_by_two_points(cls,
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
            self.x / Vector.get_length(self),
            self.y / Vector.get_length(self)
        )

    def angle_between(self, other: Vector) -> int:
        cos_a = (
            (self * other)
            / (self.get_length() * other.get_length())
        )
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 10))

    def rotate(self, degrees: int) -> Vector:
        deg_radians = math.radians(degrees)
        return Vector(
            round(
                self.x * math.cos(deg_radians)
                - self.y * math.sin(deg_radians), 2),
            round(
                self.x * math.sin(deg_radians)
                + self.y * math.cos(deg_radians), 2)
        )
