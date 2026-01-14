from __future__ import annotations
import math


class Vector:
    def __init__(self, point_x: int | float, point_y: int | float) -> None:
        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            point_x=self.x + other.x,
            point_y=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            point_x=self.x - other.x,
            point_y=self.y - other.y
        )

    def __mul__(self, other: Vector | float) -> float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(
            point_x=self.x * other,
            point_y=self.y * other
        )

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(
            point_x=end_point[0] - start_point[0],
            point_y=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return abs(math.sqrt(self.x ** 2 + self.y ** 2))

    def get_normalized(self) -> Vector:
        return Vector(
            point_x=self.x / self.get_length(),
            point_y=self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> float:
        dot_product = self.x * other.x + self.y * other.y
        magnitude_product = abs(self.get_length()) * abs(other.get_length())
        cos_theta = max(-1, min(1, dot_product / magnitude_product))

        return round(math.degrees(math.acos(cos_theta)))

    def get_angle(self) -> int:
        angle_rad = math.atan2(-self.x, self.y)
        angle_deg = math.degrees(angle_rad)

        return round(angle_deg)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
