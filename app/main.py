from __future__ import annotations

from math import sqrt, degrees, acos, atan2, cos, radians, sin


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float | int | Vector) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        magnitude = self.get_length()
        return Vector(self.x / magnitude, self.y / magnitude)

    def angle_between(self, vector: Vector) -> int:
        product = self * vector
        magnitude1 = self.get_length()
        magnitude2 = vector.get_length()
        return round(degrees(acos(product / (magnitude1 * magnitude2))))

    def get_angle(self) -> int:
        return round(abs(degrees(atan2(self.x, self.y))))

    def rotate(self, degrees: int) -> Vector:
        degrees_rad = radians(degrees)
        rotated_x = self.x * cos(degrees_rad) - self.y * sin(degrees_rad)
        rotated_y = self.x * sin(degrees_rad) + self.y * cos(degrees_rad)
        return Vector(rotated_x, rotated_y)
