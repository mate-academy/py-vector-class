from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self._x_coord = round(x_coord, 2)
        self._y_coord = round(y_coord, 2)

    @property
    def x(self) -> float:
        return self._x_coord

    @property
    def y(self) -> float:
        return self._y_coord

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(x_coord=self._x_coord + other.x,
                          y_coord=self._y_coord + other.y)

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(x_coord=self._x_coord - other.x,
                          y_coord=self._y_coord - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return (self._x_coord * other.x) + (self._y_coord * other.y)
        return Vector(x_coord=self._x_coord * other,
                      y_coord=self._y_coord * other)

    @staticmethod
    def create_vector_by_two_points(start_point: tuple,
                                    end_point: tuple) -> Vector:
        return Vector(x_coord=end_point[0] - start_point[0],
                      y_coord=end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self._x_coord ** 2 + self._y_coord ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(x_coord=self._x_coord / length,
                      y_coord=self._y_coord / length)

    def angle_between(self, other: Vector) -> int:
        dot_product = (
            self._x_coord * other.x + self._y_coord * other.y
        )
        magnitude_product = (
            math.sqrt(
                self._x_coord ** 2 + self._y_coord ** 2
            ) * math.sqrt(
                other.x ** 2 + other.y ** 2
            )
        )
        cos_angle = dot_product / magnitude_product
        angle = math.degrees(math.acos(cos_angle))
        return round(angle)

    def get_angle(self) -> int:
        positive_y_axis = Vector(x_coord=0, y_coord=1)
        return self.angle_between(positive_y_axis)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        return Vector(
            x_coord=(
                self._x_coord * math.cos(
                    radians
                ) - self._y_coord * math.sin(
                    radians
                )
            ),
            y_coord=(
                self._x_coord * math.sin(
                    radians
                ) + self._y_coord * math.cos(
                    radians
                )
            )
        )
