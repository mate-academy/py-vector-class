from __future__ import annotations
import math


class Vector:
    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float | Vector) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(x=self.x * other,
                      y=self.y * other)

    def __str__(self) -> str:
        return f"{self.x}, {self.y}"

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        x = round(end_point[0] - start_point[0], 2)
        y = round(end_point[1] - start_point[1], 2)
        return cls(x, y)

    def get_length(self) -> float:
        return round(math.sqrt(self.x ** 2 + self.y ** 2), 15)

    def get_normalized(self) -> float | Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other_vector: Vector) -> float:
        dot_product = self.x * other_vector.x + self.y * other_vector.y
        cos_a = dot_product / (self.get_length() * other_vector.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        angle_radians = math.atan2(self.x, self.y)
        angle_degrees = math.degrees(angle_radians)
        return abs(round(angle_degrees))

    def rotate(self, degrees: float) -> Vector:
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
