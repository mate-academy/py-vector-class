from __future__ import annotations
import math


class Vector:

    def __init__(self, pointx: int | float, pointy: int | float) -> None:
        self.x = round(pointx, 2)
        self.y = round(pointy, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | float | int:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0], end_point[1]
                   - start_point[1])

    def get_length(self) -> float:
        return (self.x**2 + self.y**2)**0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        dot_product = sum(i * j for i, j in zip([self.x, self.y],
                          [other.x, other.y]))
        norm_u = math.sqrt(sum(i**2 for i in [self.x, self.y]))
        norm_v = math.sqrt(sum(i**2 for i in [other.x, other.y]))
        cos_theta = dot_product / (norm_u * norm_v)
        angle_rad = math.acos(cos_theta)
        angle_deg = math.degrees(angle_rad)
        return round(angle_deg)

    def get_angle(self) -> int:
        angle_with_y_axis = math.atan2(self.x, self.y)
        angle_with_y_axis_degrees = math.degrees(angle_with_y_axis)
        return abs(round(angle_with_y_axis_degrees))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        px = self.x * math.cos(radians) - self.y * math.sin(radians)
        py = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(px, py)
