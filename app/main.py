from __future__ import annotations
from math import sin, cos, degrees, radians, acos


class Vector:
    axis_x = 0
    axis_y = 10

    def __init__(self, xx: int | float, yy: int | float) -> None:
        self.x = round(xx, 2)
        self.y = round(yy, 2)

    def __add__(self, other: Vector) -> Vector:
        self.x = self.x + other.x
        self.y = self.y + other.y
        return Vector(self.x, self.y)

    def __sub__(self, other: Vector) -> Vector:
        self.x = self.x - other.x
        self.y = self.y - other.y
        return Vector(self.x, self.y)

    def __mul__(self, other: Vector | int | float) -> Vector | float:

        if isinstance(other, Vector):
            self.x = self.x * other.x
            self.y = self.y * other.y
            return self.x + self.y

        self.x = self.x * other
        self.y = self.y * other
        return Vector(self.x, self.y)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        axis_vector_x = end_point[0] - start_point[0]
        axis_vector_y = end_point[1] - start_point[1]
        return cls(axis_vector_x, axis_vector_y)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = round(Vector(self.x, self.y).get_length(), 1)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, vector: Vector) -> float:
        length_mul = self.get_length() * vector.get_length()
        mul = self * vector
        cos = mul / length_mul
        return round(degrees(acos(cos)))

    def get_angle(self) -> float:
        return self.angle_between(Vector(Vector.axis_x, Vector.axis_y))

    def rotate(self, by_degrees: int) -> Vector:
        cos_x = self.x * cos(radians(by_degrees))
        sin_y = self.y * sin(radians(by_degrees))
        sin_x = self.x * sin(radians(by_degrees))
        cos_y = self.y * cos(radians(by_degrees))
        new_x = cos_x - sin_y
        new_y = sin_x + cos_y
        return Vector(new_x, new_y)
