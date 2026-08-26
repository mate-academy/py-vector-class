from __future__ import annotations
import math


class Vector:

    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float | Vector) -> float | Vector:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            raise TypeError("Unsupported operand type for *")

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        x = end_point[0] - start_point[0]
        y = end_point[1] - start_point[1]
        return cls(x, y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        length_product = self.get_length() * other.get_length()

        if length_product == 0:
            raise ValueError("Cannot calculate angle for a zero-length vector")

        cos_a = dot_product / length_product

        cos_a = max(-1.0, min(1.0, cos_a))

        angle_rad = math.acos(cos_a)
        angle_deg = math.degrees(angle_rad)
        return round(angle_deg,)

    def get_angle(self) -> int:
        angle_rad = math.atan2(self.x, self.y)
        angle_deg = math.degrees(angle_rad)

        if angle_deg < 0:
            angle_deg = 360 - (360 + angle_deg)

        return round(angle_deg)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_rad = math.cos(radians)
        sin_rad = math.sin(radians)

        new_x = self.x * cos_rad - self.y * sin_rad
        new_y = self.x * sin_rad + self.y * cos_rad

        return Vector(new_x, new_y)
