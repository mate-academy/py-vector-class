from __future__ import annotations
from math import acos, degrees, sqrt, sin, cos, radians


class Vector:

    def __init__(self, x_vector: float | int, y_vector: float | int) -> object:
        self.x = round(x_vector, 2)
        self.y = round(y_vector, 2)
# coment

    def __add__(self, other: Vector | float) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> int | float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        cls.x = end_point[0] - start_point[0]
        cls.y = end_point[1] - start_point[1]
        return Vector(cls.x, cls.y)

    def get_length(self) -> int | float:
        return sqrt(self.x * self.x + self.y * self.y)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize zero vector")
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        if isinstance(other, Vector):
            dot_product = self.x * other.x + self.y * other.y
            length_self = sqrt(self.x ** 2 + self.y ** 2)
            length_other = sqrt(other.x ** 2 + other.y ** 2)

            if length_self == 0 or length_other == 0:
                raise ValueError("Cannot compute angle with zero vector")

            angle_rad = acos(dot_product / (length_self * length_other))
            angle_deg = degrees(angle_rad)
            return round(angle_deg)

    def get_angle(self) -> int:

        length_self = sqrt(self.x ** 2 + self.y ** 2)
        angle_rad = acos(self.y / length_self)
        angle_deg = degrees(angle_rad)
        return round(angle_deg)

    def rotate(self, degree: int) -> Vector:
        radian_angle = radians(degree)
        new_x = self.x * cos(radian_angle) - self.y * sin(radian_angle)
        new_y = self.x * sin(radian_angle) + self.y * cos(radian_angle)
        return Vector(round(new_x, 2), round(new_y, 2))
