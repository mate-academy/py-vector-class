from __future__ import annotations
import math


class Vector:

    def __init__(
            self,
            x_axis: float | int,
            y_axis: float | int
    ) -> None:
        self.x = round(x_axis, 2)
        self.y = round(y_axis, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.x + other.x, self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x - other.x, self.y - other.y
        )

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, int | float):
            return Vector(
                other * self.x, other * self.y
            )
        else:
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return Vector(
            end_point[0] - start_point[0], end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(
            self.x / length, self.y / length
        )

    def angle_between(self, other: Vector) -> int:
        cos_a = self.__mul__(other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        cos_b = self.y / self.get_length()
        return round(math.degrees(math.acos(cos_b)))

    def rotate(self, deg: int) -> Vector:
        rd = math.radians(deg)
        x_ = self.x * math.cos(rd) - self.y * math.sin(rd)
        y_ = self.x * math.sin(rd) + self.y * math.cos(rd)
        return Vector(x_, y_)
