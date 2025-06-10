from typing import Union
from math import acos, degrees, ceil, cos, sin, radians


class Vector:

    def __init__(self, x_axis: float, y_axis: float) -> None:
        self.x = round(x_axis, 2)
        self.y = round(y_axis, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union["Vector", float]) -> Union["Vector", float]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> "Vector":
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> "Vector":
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: "Vector") -> int:
        return ceil(degrees(acos(
            Vector.__mul__(self, other)
            / (Vector.get_length(self) * Vector.get_length(other))
        )))

    def get_angle(self) -> int:
        return round(degrees(acos(
            Vector.__mul__(self, Vector(0, 1)) / (Vector.get_length(self))
        )))

    def rotate(self, degrees: int) -> "Vector":
        return Vector(
            cos(radians(degrees)) * self.x - sin(radians(degrees)) * self.y,
            sin(radians(degrees)) * self.x + cos(radians(degrees)) * self.y
        )
