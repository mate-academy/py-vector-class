from __future__ import annotations

import math


class Vector:
    def __init__(self, x_axis: float, y_axis: float) -> None:
        self.x = round(x_axis, 2)
        self.y = round(y_axis, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, factor: float | Vector) -> Vector | float:
        if isinstance(factor, (int, float)):
            return Vector(self.x * factor, self.y * factor)
        if isinstance(factor, Vector):
            return self.x * factor.x + self.y * factor.y
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(cls,
                                    point1: tuple[float, float],
                                    point2: tuple[float, float]) -> "Vector":
        """Creates a vector from two points (x1, y1) and (x2, y2)"""
        x1, y1 = point1
        x2, y2 = point2
        return cls(x2 - x1, y2 - y1)

    def get_length(self) -> float:
        """Returns the length of the vector"""
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> "Vector":
        """Returns a normalized vector (length = 1)"""
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize a zero-length vector")
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> float:
        """Returns the angle in degrees between two vectors"""
        dot_product = self.x * other.x + self.y * other.y
        length_self = self.get_length()
        length_other = other.get_length()
        if length_self == 0 or length_other == 0:
            raise ValueError("Cannot calculate angle with zero-length vector")
        cos_angle = dot_product / (length_self * length_other)
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> int:
        length = self.get_length()
        if length == 0:
            return 0  # Handle zero-vector edge case

        # Cosine of the angle relative to (0, 1) is y / length
        cos_a = self.y / length

        # Clamp to avoid floating point precision errors with acos
        cos_a = max(-1.0, min(1.0, cos_a))

        angle_rad = math.acos(cos_a)
        return round(math.degrees(angle_rad))

    def rotate(self, angle: float) -> "Vector":
        """Rotates the vector by a given angle in degrees"""
        radians = math.radians(angle)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
        x_new = self.x * cos_theta - self.y * sin_theta
        y_new = self.x * sin_theta + self.y * cos_theta
        return Vector(x_new, y_new)
