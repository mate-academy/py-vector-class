from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coordinate: int | float,
                 y_coordinate: int | float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(x_coordinate=self.x + other.x,
                          y_coordinate=self.y + other.y)
        return NotImplemented

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(x_coordinate=self.x - other.x,
                          y_coordinate=self.y - other.y)
        return NotImplemented

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        new_x = end_point[0] - start_point[0]
        new_y = end_point[1] - start_point[1]
        return cls(new_x, new_y)

    def get_length(self) -> int | float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        len1 = self.get_length()
        len2 = other.get_length()
        cos_a = (self * other) / (len1 * len2)
        cos_a = max(-1, min(1, cos_a))
        radians = math.acos(cos_a)
        degrees = math.degrees(radians)
        return int(round(degrees))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        theta = math.radians(degrees)
        new_x = self.x * math.cos(theta) - self.y * math.sin(theta)
        new_y = self.x * math.sin(theta) + self.y * math.cos(theta)
        return Vector(new_x, new_y)
