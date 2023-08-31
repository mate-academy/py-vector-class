from __future__ import annotations
import math


class Vector:
    def __init__(self, x_value: float | int, y_value: float) -> None:
        self.x = round(x_value, 2)
        self.y = round(y_value, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector) -> float | Vector:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        x_value = end_point[0] - start_point[0]
        y_value = end_point[1] - start_point[1]
        return cls(x_value, y_value)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        self_length = self.get_length()
        other_length = other.get_length()

        cos_angle = dot_product / (self_length * other_length)
        angle_in_degrees = round(math.degrees(math.acos(cos_angle)))
        return angle_in_degrees

    def get_angle(self) -> int:
        angle_radians = math.atan2(self.x, self.y)
        angle_degrees = round(math.degrees(angle_radians))
        return angle_degrees * -1

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_rad = math.cos(radians)
        sin_rad = math.sin(radians)
        new_x = self.x * cos_rad - self.y * sin_rad
        new_y = self.x * sin_rad + self.y * cos_rad
        return Vector(new_x, new_y)
