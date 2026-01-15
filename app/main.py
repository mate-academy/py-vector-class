from __future__ import annotations
import math


class Vector:
    def __init__(self, coordinate_x: float, coordinate_y: float) -> None:
        self.x: float = round(coordinate_x, 2)
        self.y: float = round(coordinate_y, 2)

    def __add__(self, other: int | float | Vector) -> int | float | Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: int | float | Vector) -> int | float | Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple
                                    ) -> int | float | Vector:
        coordinate_x: float = end_point[0] - start_point[0]
        coordinate_y: float = end_point[1] - start_point[1]
        return cls(coordinate_x, coordinate_y)

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> int | float | Vector:
        length: float = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: int | float | Vector) -> int:
        cos_angle: float = (self * other) / (self.get_length()
                                             * other.get_length())
        degrees: int = round(math.degrees(math.acos(cos_angle)))
        return degrees

    def get_angle(self) -> int:
        reference_vector: int | float | Vector = Vector(0, 1)
        return self.angle_between(reference_vector)

    def rotate(self, degrees: int) -> int | float | Vector:
        radians: float = math.radians(degrees)
        new_x: float = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y: float = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
