from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coor: int | float, y_coor: int | float) -> None:
        self.x = round(x_coor, 2)
        self.y = round(y_coor, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> int | float | Vector:
        if not isinstance(other, Vector):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        x_coor = end_point[0] - start_point[0]
        y_coor = end_point[1] - start_point[1]
        return Vector(x_coor, y_coor)

    def get_length(self) -> int | float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        if self.get_length() == 0:
            return Vector(0, 0)
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return math.ceil(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int | float:
        return round(abs(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
        x_new = self.x * cos_theta - self.y * sin_theta
        y_new = self.x * sin_theta + self.y * cos_theta
        return Vector(x_new, y_new)
