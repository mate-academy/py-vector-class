from __future__ import annotations
import math


class Vector:
    def __init__(
            self,
            coordinate_x: float,
            coordinate_y: float
    ) -> None:
        self.x: float = round(coordinate_x, 2)
        self.y: float = round(coordinate_y, 2)

    def __add__(
            self,
            other: Vector
    ) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(
            self,
            other: Vector
    ) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(
            self,
            other: float or Vector
    ) -> float or Vector:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[float, float],
            end_point: tuple[float, float]
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length: float = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(
            self,
            other: Vector
    ) -> int:
        dot_product: float = self * other
        cos_a: float = dot_product / (self.get_length() * other.get_length())
        degrees: float = math.degrees(math.acos(cos_a))
        return round(degrees)

    def get_angle(self) -> int:
        reference_vector: Vector = Vector(0, 1)
        return self.angle_between(reference_vector)

    def rotate(
            self,
            degrees: float
    ) -> Vector:
        radians: float = math.radians(degrees)
        new_x: float = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y: float = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
