from __future__ import annotations
import math


class Vector:
    def __init__(self, x_value: int, y_value: int) -> None:
        self.x = round(x_value, 2)
        self.y = round(y_value, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x=round(self.x + other.x, 2),
            y=round(self.y + other.y, 2)
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x=round(self.x - other.x, 2),
            y=round(self.y - other.y, 2)
        )

    def __mul__(self, other: Vector) -> Vector:
        if isinstance(self, Vector) and isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(
            x=round(self.x * other, 2),
            y=round(self.y * other, 2)
        )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple) -> Vector:
        return cls(
            x=end_point[0] - start_point[0],
            y=end_point[1] - start_point[1]
        )

    def get_length(self) -> int | float:
        return (self.x**2 + self.y**2) ** 0.5

    def get_normalized(self) -> Vector:
        magnitude = sum([self.x**2, self.y**2]) ** 0.5
        return Vector(x=self.x / magnitude, y=self.y / magnitude)

    def get_angle(self) -> int | float:
        angle_rad = math.atan2(self.x, self.y)
        angle_deg = math.degrees(angle_rad)
        return round(abs(angle_deg))

    def rotate(self, degrees: int | float) -> Vector:
        degrees = math.radians(degrees)
        cos_theta = math.cos(degrees)
        sin_theta = math.sin(degrees)

        nx = self.x * cos_theta - self.y * sin_theta
        ny = self.x * sin_theta + self.y * cos_theta

        return Vector(round(nx, 2), round(ny, 2))

    def angle_between(self, other: Vector) -> int:
        cos_degree = self * other / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_degree)))
