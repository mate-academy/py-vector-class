from __future__ import annotations
import math


class Vector:

    def __init__(self, axis_x: int | float, axis_y: int | float) -> None:
        self.x = round(axis_x, 2)
        self.y = round(axis_y, 2)

    def __add__(self, other: Vector) -> Vector:
        axis_x = self.x + other.x
        axis_y = self.y + other.y
        return Vector(axis_x, axis_y)

    def __sub__(self, other: Vector) -> Vector:
        axis_x = self.x - other.x
        axis_y = self.y - other.y
        return Vector(axis_x, axis_y)

    def __mul__(self, other: Vector | int) -> Vector | int:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector(
            self.x * other,
            self.y * other
        )

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

    def get_length(self) -> int | float:
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def get_normalized(self) -> Vector:
        axis_x = self.x / self.get_length()
        axis_y = self.y / self.get_length()
        return Vector(
            axis_x,
            axis_y
        )

    def angle_between(self, other: Vector) -> int:
        return round(
            math.degrees(
                math.acos(
                    self.__mul__(other)
                    / (self.get_length() * other.get_length())
                )
            )
        )

    def get_angle(self) -> int | float:
        positive_y_axis = Vector(0, 1)
        return self.angle_between(positive_y_axis)

    def rotate(self, degrees: int | float) -> Vector:
        sin = math.sin(math.radians(degrees))
        cos = math.cos(math.radians(degrees))
        axis_x = self.x * cos - self.y * sin
        axis_y = self.x * sin + self.y * cos
        return Vector(
            axis_x,
            axis_y
        )
