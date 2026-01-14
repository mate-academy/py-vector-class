from __future__ import annotations

import math


class Vector:

    def __init__(self, axes_x: float, axes_y: float) -> None:
        self.x = round(axes_x, 2)
        self.y = round(axes_y, 2)

    def __add__(self, other: Vector | int | float) -> Vector:
        return Vector(
            self.x + getattr(other, "x", other),
            self.y + getattr(other, "y", other),
        )

    def __sub__(self, other: Vector | int | float) -> Vector:
        return Vector(
            self.x - getattr(other, "x", other),
            self.y - getattr(other, "y", other),
        )

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        elif isinstance(other, Vector):
            return self.dot(other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        axes_x = end_point[0] - start_point[0]
        axes_y = end_point[1] - start_point[1]

        return cls(axes_x, axes_y)

    def get_length(self) -> float:
        return self.magnitude()

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def dot(self, other: Vector) -> float:
        return self.x * other.x + self.y * other.y

    def magnitude(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def angle_between(self, other: Vector) -> float:
        cos_angle = self.dot(other) / (self.magnitude() * other.magnitude())
        cos_angle = max(min(cos_angle, 1), -1)
        angle_rad = math.acos(cos_angle)
        angle_deg = math.degrees(angle_rad)

        return round(angle_deg)

    def get_angle(self) -> float:
        angle = math.atan2(self.x, self.y)
        return abs(round(math.degrees(angle)))

    def rotate(self, degrees: int | float) -> Vector:
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)

        return Vector(round(new_x, 2), round(new_y, 2))
