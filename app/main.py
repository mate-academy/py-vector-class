from __future__ import annotations
from typing import Union
from math import sqrt, degrees, acos, atan, cos, sin, radians


class Vector:

    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return self.create_vector_by_two_points(
            (0, 0),
            (self.x + other.x, self.y + other.y)
        )

    def __sub__(self, other: Vector) -> Vector:
        return self.create_vector_by_two_points(
            (0, 0),
            (self.x - other.x, self.y - other.y)
        )

    def __mul__(self,
                other: Union[Vector, float, int]
                ) -> Union[Vector, float]:
        if isinstance(other, float) or isinstance(other, int):
            return self.create_vector_by_two_points(
                (0, 0),
                (self.x * other, self.y * other)
            )
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple[float, float],
                                    end_point: tuple[float, float]
                                    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return self.create_vector_by_two_points(
            (0, 0),
            (self.x / self.get_length(), self.y / self.get_length())
        )

    def angle_between(self, other: Vector) -> int:
        return round(
            degrees(
                acos(
                    (self * other) / (self.get_length() * other.get_length())
                )
            )
        )

    def get_angle(self) -> int:
        if self.y > 0:
            return abs(round(degrees(atan(self.x / self.y))))
        if self.y < 0:
            return abs(180 - round(degrees(atan(self.x / self.y))))

    def rotate(self, angle: int) -> Vector:
        radian = radians(angle)
        rotated_x = self.x * cos(radian) - self.y * sin(radian)
        rotated_y = self.x * sin(radian) + self.y * cos(radian)
        return self.create_vector_by_two_points(
            (0, 0),
            (rotated_x, rotated_y)
        )
