from __future__ import annotations
import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float) -> float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple[float, float],
        end_point: tuple[float, float],
    ) -> "Vector":
        x_diff = end_point[0] - start_point[0]
        y_diff = end_point[1] - start_point[1]
        return cls(x_diff, y_diff)

    def get_length(self) -> float:
        return math.hypot(self.x, self.y)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, vector: "Vector") -> int:
        dot = self * vector
        len_mul = self.get_length() * vector.get_length()
        cos_a = max(min(dot / len_mul, 1), -1)
        angle_rad = math.acos(cos_a)
        return round(math.degrees(angle_rad))

    def get_angle(self) -> int:
        angle_rad = math.atan2(-self.x, self.y)
        return round(math.degrees(angle_rad))

    def rotate(self, degrees: int) -> "Vector":
        rad = math.radians(degrees)
        cos_a = math.cos(rad)
        sin_a = math.sin(rad)
        x_new = self.x * cos_a - self.y * sin_a
        y_new = self.x * sin_a + self.y * cos_a
        return Vector(x_new, y_new)
