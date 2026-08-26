from __future__ import annotations
import math


class Vector:

    def __init__(self, x_coor: float, y_coor: float) -> None:
        self.x = round(x_coor, 2)
        self.y = round(y_coor, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector(self.x * other, self.y * other)

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int | float:
        mul = self * other
        current_length = self.get_length()
        other_length = other.get_length()
        cos_a = mul / (current_length * other_length)
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int | float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        x_coor = ((math.cos(math.radians(degrees)) * self.x)
                  - (math.sin(math.radians(degrees)) * self.y))
        y_coor = ((math.sin(math.radians(degrees)) * self.x)
                  + (math.cos(math.radians(degrees)) * self.y))
        return Vector(x_coor, y_coor)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])
