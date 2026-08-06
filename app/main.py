from __future__ import annotations

import math


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector or float) -> Vector or float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        start_x, start_y = start_point
        end_x, end_y = end_point
        x_coord = end_x - start_x
        y_coord = end_y - start_y
        return cls(x_coord, y_coord)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        self_length = self.get_length()
        other_length = other.get_length()
        cos_angle = dot_product / (self_length * other_length)
        angle_deg = round(math.degrees(math.acos(cos_angle)))
        return angle_deg

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        theta_rad = math.radians(degrees)
        cos_theta = math.cos(theta_rad)
        sin_theta = math.sin(theta_rad)
        x_rotated = self.x * cos_theta - self.y * sin_theta
        y_rotated = self.x * sin_theta + self.y * cos_theta
        return Vector(x_rotated, y_rotated)
