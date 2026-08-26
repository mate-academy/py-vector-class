from __future__ import annotations
from math import degrees, acos, cos, sin, radians


class Vector:
    def __init__(self, x_axis: float, y_axis: float) -> None:
        self.x = round(x_axis, 2)
        self.y = round(y_axis, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float | Vector) -> float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @staticmethod
    def create_vector_by_two_points(
            start_point: tuple,
            end_point: tuple) -> Vector:
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(),
                      self.y / self.get_length())

    def angle_between(self, vector: Vector) -> int:
        cos_a = (((self.x * vector.x)
                  + (self.y * vector.y))
                 / (self.get_length() * vector.get_length()))
        return round(degrees(acos(cos_a)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, rotate_degrees: int) -> Vector:
        rotate_degrees = radians(rotate_degrees)
        cos_a = cos(rotate_degrees)
        sin_a = sin(rotate_degrees)
        print(cos_a, sin_a)
        rotated_x = self.x * cos_a - self.y * sin_a
        rotated_y = self.x * sin_a + self.y * cos_a
        return Vector(rotated_x, rotated_y)
