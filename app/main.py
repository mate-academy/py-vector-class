from __future__ import annotations
import math


class Vector:
    def __init__(self, x_point: float | int, y_point: float | int) -> "Vector":
        self.x = round(x_point, 2)
        self.y = round(y_point, 2)

    def __add__(self, other: Vector) -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector) -> "Vector":
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        else:
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> object:
        x_point = round(end_point[0] - start_point[0], 2)
        y_point = round(end_point[1] - start_point[1], 2)
        return cls(x_point, y_point)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> float:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> Vector:
        dot_product = self * other
        cos_a = dot_product / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> Vector:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        radians_value = math.radians(degrees)
        x_point = round(self.x * math.cos(radians_value)
                        - self.y * math.sin(radians_value), 2)
        y_point = round(self.x * math.sin(radians_value)
                        + self.y * math.cos(radians_value), 2)
        return Vector(x_point, y_point)
