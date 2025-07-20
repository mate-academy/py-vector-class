from __future__ import annotations
import math


class Vector:
    # write your code here
    pass

    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return NotImplemented

    def __rmul__(self, other: int | float) -> Vector:
        return self * other

    def dot(self, other: Vector) -> float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[float, float],
            end_point: tuple[float, float]
    ) -> Vector:
        x1, y1 = start_point
        x2, y2 = end_point
        return Vector(x2 - x1, y2 - y1)

    def get_length(self) -> float:
        return math.hypot(self.x, self.y)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize a zero-length vector")
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        dot_product = self.dot(other)
        len_self = self.get_length()
        len_other = other.get_length()
        if len_self == 0 or len_other == 0:
            raise ValueError("Cannot compute angle with zero-length vector")
        cos_a = dot_product / (len_self * len_other)
        cos_a = max(min(cos_a, 1), -1)
        angle_deg = math.degrees(math.acos(cos_a))
        return round(angle_deg)

    def get_angle(self) -> int:
        length = self.get_length()
        if length == 0:
            raise ValueError("Zero-length vector has no angle with Y axis.")
        cos_theta = self.y / length
        cos_theta = max(min(cos_theta, 1), -1)
        angle_rad = math.acos(cos_theta)
        angle_deg = math.degrees(angle_rad)
        return round(angle_deg)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_a = math.cos(radians)
        sin_a = math.sin(radians)
        new_x = self.x * cos_a - self.y * sin_a
        new_y = self.x * sin_a + self.y * cos_a
        return Vector(round(new_x, 2), round(new_y, 2))
