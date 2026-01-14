from __future__ import annotations

import math


class Vector:
    def __init__(self, cord_x: int | float, cord_y: int | float) -> None:
        self.x = round(cord_x, 2)
        self.y = round(cord_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float | int) -> float | "Vector":
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> "Vector":
        x_start, y_start = start_point
        x_end, y_end = end_point
        return cls(x_end - x_start, y_end - y_start)

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        length_product = self.get_length() * other.get_length()
        if length_product == 0:
            return 0
        cos_angle = dot_product / length_product
        cos_angle = max(-1, min(1, cos_angle))  # Clamp value between -1 and 1
        angle_rad = math.acos(cos_angle)
        angle_deg = math.degrees(angle_rad)
        return round(angle_deg)

    def get_angle(self) -> float:
        angle_rad = math.atan2(self.x, self.y)
        angle_deg = math.degrees(angle_rad)
        return abs(round(angle_deg))

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(round(new_x, 2), round(new_y, 2))

    def __repr__(self) -> str:
        return f"Vector(x={self.x}, y={self.y})"
