from __future__ import annotations
import math


class Vector:
    def __init__(
            self,
            coordinate_x: float | int,
            coordinate_y: float | int,
    ) -> None:
        self.x = round(coordinate_x, 2)
        self.y = round(coordinate_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> int | float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple,
        end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize a zero vector")
        return Vector(self.x / length, self.y / length)

    def angle_between(self, vector: "Vector") -> int:
        denominator = self.get_length() * vector.get_length()
        if denominator == 0:
            raise ValueError("Cannot calculate angle with a zero vector")
        cos_a = (self * vector) / denominator
        cos_a = max(-1.0, min(1.0, cos_a))
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return round(math.degrees(math.atan2(abs(self.x), self.y)))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        rotated_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        rotated_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(rotated_x, rotated_y)
