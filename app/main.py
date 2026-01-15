from __future__ import annotations
from math import sin, cos, sqrt, acos, degrees, radians


class Vector:

    def __init__(self,
                 x_coord: int | float,
                 y_coord: int | float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self,
                other: Vector) -> Vector:
        return Vector(x_coord=self.x + other.x,
                      y_coord=self.y + other.y)

    def __sub__(self,
                other: Vector) -> Vector:
        return Vector(x_coord=self.x - other.x,
                      y_coord=self.y - other.y)

    def __mul__(self,
                other:
                int | float | Vector) -> int | float | Vector:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector(x_coord=self.x * other,
                      y_coord=self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start: tuple,
                                    end: tuple) -> Vector:
        return cls(x_coord=end[0] - start[0],
                   y_coord=end[1] - start[1])

    def get_length(self) -> int | float:
        return sqrt((self.x ** 2) + (self.y ** 2))

    def get_normalized(self) -> Vector:
        return Vector(x_coord=round(self.x / self.get_length(), 2),
                      y_coord=round(self.y / self.get_length(), 2))

    def angle_between(self,
                      other: Vector) -> int | float:
        dot_product = (self.x * other.x) + (self.y * other.y)
        magnitudes_first_vector = sqrt((self.x ** 2) + (self.y ** 2))
        magnitudes_second_vector = sqrt((other.x ** 2) + (other.y ** 2))
        cos_a = (dot_product
                 / (magnitudes_first_vector * magnitudes_second_vector))
        angle = degrees(acos(cos_a))
        return round(angle)

    def get_angle(self) -> int | float:
        dot_product = (self.x * 0) + (self.y * 1)
        magnitude = sqrt((self.x ** 2) + (self.y ** 2))
        cos_a = dot_product / magnitude
        angle = degrees(acos(cos_a))
        return round(angle)

    def rotate(self, rotation_degrees: int) -> Vector:
        radian = radians(rotation_degrees)
        rotated_x = (cos(radian) * self.x) - (sin(radian) * self.y)
        rotated_y = (sin(radian) * self.x) + (cos(radian) * self.y)
        return Vector(x_coord=rotated_x, y_coord=rotated_y)
