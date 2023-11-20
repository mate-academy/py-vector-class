from __future__ import annotations
import math


class Vector:
    def __init__(
            self,
            x_coordinate: float | int,
            y_coordinate: float | int
    ) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | float | int:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, int) or isinstance(other, float):
            self.x = round(self.x * other, 2)
            self.y = round(self.y * other, 2)
            return self

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return self * (1 / self.get_length())

    def angle_between(self, other: Vector) -> float | int:
        return round(
            math.degrees(
                math.acos((self * other)
                          / (((self.x ** 2 + self.y ** 2) ** 0.5)
                             * ((other.x ** 2 + other.y ** 2) ** 0.5))))
        )

    def get_angle(self) -> float | int:
        axis_y_vector = Vector(0, 1)
        return self.angle_between(axis_y_vector)

    def rotate(self, degrees: int) -> Vector:
        return Vector(math.cos(math.radians(degrees)) * self.x
                      - math.sin(math.radians(degrees)) * self.y,
                      math.sin(math.radians(degrees)) * self.x
                      + math.cos(math.radians(degrees)) * self.y)
