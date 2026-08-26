from typing import Any
import math


class Vector:

    def __init__(self, x_cordinate: float, y_cordinate: float) -> None:
        self.x = round(x_cordinate, 2)
        self.y = round(y_cordinate, 2)

    def __add__(self, other: float) -> Any:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other: float) -> Any:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, other: float) -> Any:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return NotImplemented

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple,
        end_point: tuple
    ) -> Any:
        x_cordinate = round(end_point[0] - start_point[0], 2)
        y_cordinate = round(end_point[1] - start_point[1], 2)
        return cls(x_cordinate, y_cordinate)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> float:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: int) -> float:
        length_self = self.get_length()
        length_other = other.get_length()
        if length_self == 0 or length_other == 0:
            raise ValueError
        dot_product = self.x * other.x + self.y * other.y
        cos_theta = dot_product / (length_self * length_other)
        cos_theta = max(-1, min(1, cos_theta))
        angle_rad = math.acos(cos_theta)
        angle_deg = math.degrees(angle_rad)
        return round(angle_deg)

    def get_angle(self) -> int:
        angle_r = math.atan2(self.x, self.y)
        angle_d = math.degrees(angle_r)
        return abs(round(angle_d))

    def rotate(self, degrees: float) -> "Vector":
        radians = math.radians(degrees)
        x_new = self.x * math.cos(radians) - self.y * math.sin(radians)
        y_new = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(round(x_new, 2), round(y_new, 2))
