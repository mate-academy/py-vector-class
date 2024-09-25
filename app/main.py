from __future__ import annotations

import math

import numpy as np


class Vector:
    def __init__(self, coord_x: float | int, coord_y: float | int) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: Vector | float | int) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector | float | int) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float | int) -> float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        start_x, start_y = start_point
        end_x, end_y = end_point
        return cls(end_x - start_x, end_y - start_y)

    def get_length(self) -> Vector:
        return abs(np.hypot(self.x, self.y))

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector | float | int) -> Vector:
        dot_product = self.x * other.x + self.y * other.y  # -34
        get_magnitude = self.get_length() * other.get_length()
        rad_angel = np.arccos(dot_product / get_magnitude)
        result = np.degrees(rad_angel)
        return round(result)

    def get_angle(self) -> Vector | int | float:
        angle = math.degrees(math.atan2(-self.x, self.y)) % 360
        return round(angle)

    def rotate(self, other: Vector | float | int) -> Vector:
        radians = math.radians(other)
        cos_angle = math.cos(radians)
        sin_angle = math.sin(radians)
        rot_x = self.x * cos_angle - self.y * sin_angle
        rot_y = self.x * sin_angle + self.y * cos_angle
        return Vector(rot_x, rot_y)
