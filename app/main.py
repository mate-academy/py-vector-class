from __future__ import annotations
import math


class Vector:
    def __init__(self, cor_x: int, cor_y: int) -> None:
        self.x = round(cor_x, 2)
        self.y = round(cor_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector((self.x + other.x), (self.y + other.y))

    def __sub__(self, other: Vector) -> Vector:
        return Vector((self.x - other.x), (self.y - other.y))

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, (int, float)):
            self.x = round((self.x * other), 2)
            self.y = round((self.y * other), 2)
            return self
        return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        new_x = end_point[0] - start_point[0]
        new_y = end_point[1] - start_point[1]
        return cls(new_x, new_y)

    def get_length(self) -> float:
        return (self.x**2 + self.y**2)**0.5

    def get_normalized(self) -> float:
        length = self.get_length()
        self.x = round((self.x / length), 2)
        self.y = round((self.y / length), 2)
        return self

    def angle_between(self, other: Vector) -> float:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        vector_y = Vector(0, 1)
        return self.angle_between(vector_y)

    def rotate(self, degrees: int) -> Vector:
        degrees = math.radians(degrees)
        new_x = round((math.cos(degrees) * self.x
                       - math.sin(degrees) * self.y), 2)
        new_y = round((math.sin(degrees) * self.x
                       + math.cos(degrees) * self.y), 2)
        self.x, self.y = new_x, new_y
        return self
