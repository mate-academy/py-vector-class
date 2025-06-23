from __future__ import annotations
from math import sqrt
from math import acos
from math import degrees
from math import radians
from math import cos
from math import sin


class Vector:
    def __init__(self, x_coord: int | float, y_coord: int | float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x_coord=self.x + other.x,
            y_coord=self.y + other.y,
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x_coord=self.x - other.x,
            y_coord=self.y - other.y,
        )

    def __mul__(self, other: int | float | Vector) -> int | float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(
                x_coord=self.x * other,
                y_coord=self.y * other,
            )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[int | float, int | float],
            end_point: tuple[int | float, int | float],
    ) -> Vector:
        return cls(
            x_coord=end_point[0] - start_point[0],  # x2 - x1
            y_coord=end_point[1] - start_point[1]  # y2 - y1
        )

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            x_coord=self.x / self.get_length(),
            y_coord=self.y / self.get_length(),
        )

    def angle_between(self, other: Vector) -> float | int:
        cos_theta = (
            self.__mul__(other)
            / (self.get_length() * other.get_length())
        )
        theta_radians = acos(cos_theta)
        return round(degrees(theta_radians))

    def get_angle(self) -> float:
        cos_theta = self.y / self.get_length()
        theta_radians = acos(cos_theta)
        return round(degrees(theta_radians))

    def rotate(self, degrees: float | int) -> Vector:
        theta = radians(degrees)
        return Vector(
            x_coord=self.x * cos(theta) - self.y * sin(theta),
            y_coord=self.x * sin(theta) + self.y * cos(theta)
        )
