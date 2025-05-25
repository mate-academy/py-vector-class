from __future__ import annotations
from math import sin, cos, sqrt, acos, degrees, radians


class Vector:

    def __init__(self,
                 x: int | float,
                 y: int | float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self,
                other: Vector) -> Vector:
        return Vector(x=self.x + other.x,
                      y=self.y + other.y)

    def __sub__(self,
                other: Vector) -> Vector:
        return Vector(x=self.x - other.x,
                      y=self.y - other.y)

    def __mul__(self,
                other:
                int | float | Vector) -> int | float | Vector:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector(x=self.x * other,
                      y=self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start: tuple,
                                    end: tuple) -> Vector:
        return cls(x=end[0] - start[0],
                   y=end[1] - start[1])

    def get_length(self) -> int | float:
        return sqrt((self.x ** 2) + (self.y ** 2))

    def get_normalized(self) -> Vector:
        return Vector(x=round(self.x / self.get_length(), 2),
                      y=round(self.y / self.get_length(), 2))

    def angle_between(self,
                      other: Vector) -> int | float:
        dot_product = (self.x * other.x) + (self.y * other.y)
        magnitudes_first_vector = sqrt((self.x ** 2) + (self.y ** 2))
        magnitudes_second_vector = sqrt((other.x ** 2) + (other.y ** 2))
        cos_a = (dot_product /
                 (magnitudes_first_vector * magnitudes_second_vector))
        angle = degrees(acos(cos_a))
        return round(angle)

    def get_angle(self) -> int | float:
        dot_product = (self.x * 0) + (self.y * 1)
        magnitude = sqrt((self.x ** 2) + (self.y ** 2))
        cos_a = dot_product / magnitude
        angle = degrees(acos(cos_a))
        return round(angle)

    def rotate(self, rotation_degrees: int) -> Vector:
        rotate_to_radians = radians(rotation_degrees)
        return Vector(x=(cos(rotate_to_radians) * self.x) -
                        (sin(rotate_to_radians) * self.y),
                      y=(sin(rotate_to_radians) * self.x) +
                        (cos(rotate_to_radians) * self.y))










