from __future__ import annotations
import math


class Vector:
    def __init__(self, x_axis: float, y_axis: float) -> None:
        self.x = round(x_axis, 2)
        self.y = round(y_axis, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector((self.x + other.x), (self.y + other.y))

    def __sub__(self, other: Vector) -> Vector:
        return Vector((self.x - other.x), (self.y - other.y))

    def __mul__(self, other: float | Vector) -> float | Vector:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector(round(self.x * other, 2), round(self.y * other, 2))

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls((end_point[0] - start_point[0]),
                   (end_point[1] - start_point[1]))

    def get_length(self) -> float:
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector((self.x / self.get_length()),
                      (self.y / self.get_length()))

    def angle_between(self, vector: Vector) -> int:
        dot_product = (self.x * vector.x) + (self.y * vector.y)
        cos_theta = dot_product / (self.get_length() * vector.get_length())
        return round(math.degrees(math.acos(cos_theta)))

    def get_angle(self) -> int:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degrees: int) -> Vector:
        return Vector(round(self.x * math.cos(math.radians(degrees))
                            - self.y * math.sin(math.radians(degrees)), 2),
                      round(self.x * math.sin(math.radians(degrees))
                            + self.y * math.cos(math.radians(degrees)), 2))
