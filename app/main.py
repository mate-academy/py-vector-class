from __future__ import annotations
import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: int) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: int) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            raise TypeError(
                "Vector can be multiplied only by int, float, or Vector"
            )

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple) -> Vector:
        return Vector(
            end_point[0] - start_point[0], end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize zero vector")
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        dot = self.x * other.x + self.y * other.y
        len1 = self.get_length()
        len2 = other.get_length()
        if len1 == 0 or len2 == 0:
            raise ValueError("Cannot angle vector with zero length")
        cos_a = dot / (len1 * len2)
        cos_a = min(1.0, max(-1.0, cos_a))
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        len1 = self.get_length()
        if len1 == 0:
            raise ValueError("Cannot angle vector with zero length")
        cos_a = self.y / len1
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        variable_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        variable_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(round(variable_x, 2), round(variable_y, 2))
