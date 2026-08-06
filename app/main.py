from typing import Any

import math


class Vector:
    def __init__(self, pos_x: int | float, pos_y: int | float) -> None:
        self.x = round(pos_x, 2)
        self.y = round(pos_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, scalar: Any) -> Any:
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        if isinstance(scalar, Vector):
            return self.x * scalar.x + self.y * scalar.y
        return NotImplemented

    def get_length(self) -> int | float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> "Vector":
        magnitude = self.get_length()
        return Vector(self.x / magnitude, self.y / magnitude)

    def angle_between(self, second_vector: "Vector") -> int | float:
        magnitude_first = self.get_length()
        magnitude_second = second_vector.get_length()
        dot_product = self * second_vector
        cos_angle = dot_product / (magnitude_first * magnitude_second)
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> int:
        angle_rad = math.atan2(self.x, self.y)
        angle_deg = math.degrees(angle_rad)
        if angle_deg < 0:
            return round(abs(angle_deg))
        return round(angle_deg)

    def rotate(self, degrees: int) -> "Vector":
        radian_angle = math.radians(degrees)
        cos_angle = math.cos(radian_angle)
        sin_angle = math.sin(radian_angle)
        rotated_x = cos_angle * self.x - sin_angle * self.y
        rotated_y = sin_angle * self.x + cos_angle * self.y
        return Vector(rotated_x, rotated_y)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> "Vector":
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )
