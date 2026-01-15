from __future__ import annotations
import math


class Vector:
    def __init__(self, _x: float, _y: float) -> None:
        self.x = round(_x, 2)
        self.y = round(_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        start_x, start_y = start_point[0], start_point[1]
        end_x, end_y = end_point[0], end_point[1]
        return cls(end_x - start_x, end_y - start_y)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return self * (1 / self.get_length())

    def angle_between(self, other: Vector) -> int:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        degrees = (math.radians(degrees))
        new_x = self.x * math.cos(degrees) - self.y * math.sin(degrees)
        new_y = self.x * math.sin(degrees) + self.y * math.cos(degrees)
        return Vector(new_x, new_y)
