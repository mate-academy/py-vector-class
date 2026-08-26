from __future__ import annotations
import math


class Vector:
    # write your code here
    def __init__(self, x_coords: float, y_coords: float) -> None:
        self.x = round(x_coords, 2)
        self.y = round(y_coords, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, other: int | float | Vector) -> float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(
            self.x * other,
            self.y * other
        )

    @classmethod
    def create_vector_by_two_points(
            cls,
            point1: tuple,
            point2: tuple
    ) -> Vector:
        return Vector(
            point2[0] - point1[0],
            point2[1] - point1[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def angle_between(self, other: Vector) -> int:
        cos_angle = (self * other) / (self.get_length() * other.get_length())
        angle_degrees = math.degrees(math.acos(cos_angle))
        return round(angle_degrees)

    def get_normalized(self) -> Vector:
        if self.get_length() == 0:
            return self
        return Vector(
            round((self.x / self.get_length()), 2),
            round((self.y / self.get_length()), 2)
        )

    def get_angle(self) -> int:
        cos_theta = self.y / self.get_length()
        theta_rad = math.acos(cos_theta)
        theta_deg = math.degrees(theta_rad)
        return round(theta_deg)

    def rotate(self, degree: int) -> Vector:
        theta_rad = math.radians(degree)
        cos_theta = math.cos(theta_rad)
        sin_theta = math.sin(theta_rad)

        return Vector(
            self.x * cos_theta - self.y * sin_theta,
            self.x * sin_theta + self.y * cos_theta
        )
