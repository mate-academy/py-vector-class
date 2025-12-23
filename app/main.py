from __future__ import annotations
import math


class Vector:
    def __init__(self, x_point: int | float, y_point: int | float) -> None:
        self.x = round(x_point, 2)
        self.y = round(y_point, 2)

    def __add__(self, other: Vector) -> Vector:
        x_point = round(self.x + other.x, 2)
        y_point = round(self.y + other.y, 2)
        return Vector(x_point, y_point)

    def __sub__(self, other: Vector) -> Vector:
        x_point = round(self.x - other.x, 2)
        y_point = round(self.y - other.y, 2)
        return Vector(x_point, y_point)

    def __mul__(self, other: int | float | Vector) -> Vector | int:
        if isinstance(other, int) or isinstance(other, float):
            x_point = round(self.x * other, 2)
            y_point = round(self.y * other, 2)
            return Vector(x_point, y_point)

        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple
                                    ) -> Vector:
        x_point = end_point[0] - start_point[0]
        y_point = end_point[1] - start_point[1]
        return cls(x_point, y_point)

    def get_length(self) -> int | float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        new_vector = self.get_length()
        return Vector(self.x / new_vector, self.y / new_vector)

    def angle_between(self, other: Vector) -> int:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        cos_a = (self.x * 0 + self.y
                 * ((self.y ** 2) ** 0.5)) / (self.get_length()
                                              * Vector(0, self.y).get_length())
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, other: int) -> Vector:
        x_point_1 = math.cos(math.radians(other)) * self.x
        x_point_2 = math.sin(math.radians(other)) * self.y
        x_point = x_point_1 - x_point_2
        y_point_1 = math.sin(math.radians(other)) * self.x
        y_point_2 = math.cos(math.radians(other)) * self.y
        y_point = y_point_1 + y_point_2
        return Vector(x_point, y_point)
