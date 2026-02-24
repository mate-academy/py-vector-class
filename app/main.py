from __future__ import annotations
import math


class Vector:
    def __init__(self, x_axis: float, y_axis: float) -> None:
        self.x = round(x_axis, 2)
        self.y = round(y_axis, 2)

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
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0.0, 0.0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        dot = self * other
        len_self = self.get_length()
        len_other = other.get_length()

        if len_self == 0 or len_other == 0:
            return 0

        cos_angle = dot / (len_self * len_other)
        cos_angle = max(-1.0, min(1.0, cos_angle))
        angle_rad = math.acos(cos_angle)
        angle_deg = math.degrees(angle_rad)
        return int(round(angle_deg))

    def get_angle(self) -> int:
        length = self.get_length()
        if length == 0:
            return 0

        cos_angle = self.y / length
        cos_angle = max(-1.0, min(1.0, cos_angle))
        angle_rad = math.acos(cos_angle)
        angle_deg = math.degrees(angle_rad)
        return int(round(angle_deg))

    def rotate(self, degrees: int) -> Vector:
        if self.x == 0 and self.y == 0:
            return Vector(0.0, 0.0)

        theta = math.radians(degrees)
        cos_theta = math.cos(theta)
        sin_theta = math.sin(theta)

        x_new = self.x * cos_theta - self.y * sin_theta
        y_new = self.x * sin_theta + self.y * cos_theta

        return Vector(x_new, y_new)
