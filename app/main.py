from __future__ import annotations
import math


class Vector:
    def __init__(self, x_value: float, y_value: float) -> None:
        self.x = round(x_value, 2)
        self.y = round(y_value, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> int:
        dot_product = self.__mul__(other)
        magnitude = self.get_length() * other.get_length()
        tmp_value = dot_product / magnitude
        return round(math.degrees(math.acos(tmp_value)))

    def get_angle(self) -> int:
        y_axis = Vector(0, 10)
        dot_product = self.__mul__(y_axis)
        magnitude = self.get_length() * y_axis.get_length()
        tmp_value = dot_product / magnitude
        return round(math.degrees(math.acos(tmp_value)))

    def rotate(self, degrees: int) -> Vector:
        degrees = math.radians(degrees)
        return Vector(
            math.cos(degrees) * self.x - math.sin(degrees) * self.y,
            math.sin(degrees) * self.x + math.cos(degrees) * self.y
        )
