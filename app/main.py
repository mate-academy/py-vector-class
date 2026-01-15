from __future__ import annotations
import math


class Vector:
    def __init__(self, xxx: float, yyy: float) -> None:
        self.x = round(xxx, 2)
        self.y = round(yyy, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float | Vector) -> float | Vector:
        if isinstance(other, Vector):
            return round(self.x * other.x + self.y * other.y, 14)
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple[float, float],
                                    end_point: tuple[float, float]
                                    ) -> Vector:
        xxx = end_point[0] - start_point[0]
        yyy = end_point[1] - start_point[1]
        return cls(xxx, yyy)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize a zero-length vector.")
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        magnitude_product = self.get_length() * other.get_length()
        if magnitude_product == 0:
            raise ValueError("Cannot calculate angle with zero-length vector.")
        cos_angle = dot_product / magnitude_product
        angle = math.degrees(
            math.acos(
                max(
                    -1, min(1, cos_angle)
                )
            )
        )
        return round(angle)

    def get_angle(self) -> int:
        vertical = Vector(0, 1)
        return self.angle_between(vertical)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
        xxx = self.x * cos_theta - self.y * sin_theta
        yyy = self.x * sin_theta + self.y * cos_theta
        return Vector(xxx, yyy)
