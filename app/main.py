from __future__ import annotations
import math


class Vector:
    def __init__(self, x_point: int, y_point: int) -> None:
        self.x = round(x_point, 2)
        self.y = round(y_point, 2)

    def __add__(self, other: int | float | Vector) -> object:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: int | float | Vector) -> object:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> object:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> object:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> object:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: int | float | Vector) -> int:
        dot_product = self * other
        cos_angle = dot_product / (self.get_length() * other.get_length())
        degrees = math.degrees(math.acos(cos_angle))
        return round(degrees)

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> object:
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
