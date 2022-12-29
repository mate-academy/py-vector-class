from __future__ import annotations
import math


class Vector:

    def __init__(self, x_value: float, y_value: float) -> None:
        self.x = round(x_value, 2)
        self.y = round(y_value, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x_value=self.x + other.x,
            y_value=self.y + other.y,
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x_value=self.x - other.x,
            y_value=self.y - other.y,
        )

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
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
            (end_point[0]) - (start_point[0]),
            (end_point[1]) - (start_point[1])
        )

    def get_length(self) -> int | float:
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(
            x_value=self.x / length,
            y_value=self.y / length
        )

    def angle_between(self, other: Vector) -> int:
        length_self = self.get_length()
        length_other = other.get_length()
        dot_product = self * other
        cos_a = dot_product / (length_self * length_other)
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        x_value = (math.cos(math.radians(degrees)) * self.x) - \
                  (math.sin(math.radians(degrees)) * self.y)
        y_value = (math.sin(math.radians(degrees)) * self.x) + \
                  (math.cos(math.radians(degrees)) * self.y)
        return Vector(
            x_value,
            y_value
        )
