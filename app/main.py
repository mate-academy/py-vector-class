from __future__ import annotations
import math


class Vector:

    def __init__(self, x: int | float, y: int | float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector(
            x=self.x * other,
            y=self.y * other
        )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: int | float,
            end_point: int | float
    ) -> Vector:

        return cls(
            x=end_point[0] - start_point[0],
            y=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt((self.x ** 2 + self.y ** 2))

    def get_normalized(self) -> Vector:
        vector_length = self.get_length()
        normalized_x = round(self.x / vector_length, 2)
        normalized_y = round(self.y / vector_length, 2)

        return Vector(normalized_x, normalized_y)

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        cos_a = dot_product / (self.get_length() * other.get_length())
        result = math.degrees(math.acos(cos_a))
        return round(result)

    def get_angle(self) -> int:
        other = Vector(0, 1)
        return self.angle_between(other)

    def rotate(self, degrees: int) -> Vector:
        cos = math.cos(math.radians(degrees))
        sin = math.sin(math.radians(degrees))
        rotated_x = cos * self.x - sin * self.y
        rotated_y = sin * self.x + cos * self.y
        return Vector(rotated_x, rotated_y)
