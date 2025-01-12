from __future__ import annotations
from typing import Union, Any
from math import acos, degrees, radians, sqrt, sin, cos, atan2


class Vector:

    def __init__(self, x_axis: float, y_axis: float) -> None:
        self.x = round(x_axis, 2)
        self.y = round(y_axis, 2)

    def __add__(self, other: Any) -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union["Vector", int, float]) -> "Vector":
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
        cls,
        point1: tuple,
        point2: tuple
    ) -> "Vector":
        return cls(
            round(point2[0] - point1[0], 2),
            round(point2[1] - point1[1], 2)
        )

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize the zero-length vector")
        return Vector(
            self.x / length,
            self.y / length
        )

    def angle_between(self, other: "Vector") -> float:
        distance1 = self.get_length()
        distance2 = other.get_length()
        if distance1 == 0 or distance2 == 0:
            raise ValueError(
                "Cannot calculate the angle between zero-length vector"
            )
        product = self.x * other.x + self.y * other.y
        return round(degrees(acos(
            max(-1, min(1, product / (distance1 * distance2)))
        )))

    def get_angle(self) -> float:
        return abs(round(degrees(atan2(self.x, self.y))))
        # return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: float) -> "Vector":
        deg_of_radians = radians(degrees)

        return Vector(
            round(
                self.x * cos(deg_of_radians) - self.y * sin(deg_of_radians)
                , 2
            ),
            round(
                self.x * sin(deg_of_radians) + self.y * cos(deg_of_radians)
                , 2
            )
        )
