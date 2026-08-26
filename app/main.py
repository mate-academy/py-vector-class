from math import sqrt, degrees, radians, acos, cos, sin
from typing import Union


class Vector:
    def __init__(self, x: int, y: int) -> None:  # noqa: VNE001
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(
            self,
            other: Union["Vector", int]
    ) -> Union["Vector", float, int]:

        if not isinstance(other, Vector):
            return Vector(
                self.x * other,
                self.y * other
            )
        else:
            return (
                self.x * other.x + self.y * other.y
            )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> "Vector":

        vector_end = Vector(*end_point)
        vector_start = Vector(*start_point)
        return vector_end - vector_start

    def get_length(self) -> float:
        return sqrt(pow(self.x, 2) + pow(self.y, 2))

    def get_normalized(self) -> "Vector":
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: "Vector") -> int:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(degrees(acos(cos_a)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, rotate_degrees: int | float) -> "Vector":
        rotate_degrees = radians(rotate_degrees)
        x_r = self.x * cos(rotate_degrees) - self.y * sin(rotate_degrees)
        y_r = self.x * sin(rotate_degrees) + self.y * cos(rotate_degrees)
        return Vector(x_r, y_r)
