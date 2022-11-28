from __future__ import annotations
import math


class Vector:
    def __init__(self, side_x: int, side_y: int) -> None:
        self.side_x = round(side_x, 2)
        self.side_y = round(side_y, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.side_x + other.side_x,
                          self.side_y + other.side_y)

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.side_x - other.side_x,
                          self.side_y - other.side_y)

    def __mul__(self, other: int | float | Vector) -> Vector | int | float:
        if isinstance(other, (int, float)):
            return Vector(self.side_x * other, self.side_y * other)
        if isinstance(other, Vector):
            return (self.side_x * other.side_x) + (self.side_y * other.side_y)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple,
            end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.side_x ** 2 + self.side_y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.side_x / length, self.side_y / length)

    def angle_between(self, other: Vector) -> int:
        cos_a = ((self.side_x * other.side_x)
                 + (self.side_y * other.side_y)) / \
                ((self.get_length() * other.get_length()))
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return round(math.degrees(math.acos(
            self.side_y / (self.get_length()))))

    def rotate(self, degrees: int) -> Vector:
        x2 = math.cos(math.radians(degrees))
        y2 = math.sin(math.radians(degrees))
        return Vector((self.side_x * x2 - y2 * self.side_y),
                      (self.side_x * y2 + x2 * self.side_y))
