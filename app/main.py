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

    def __mul__(self, other: float | Vector) -> float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            x_other = self.x * other
            y_other = self.y * other
        return Vector(x_other, y_other)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        x_new = end_point[0] - start_point[0]
        y_new = end_point[1] - start_point[1]
        return Vector(x_new, y_new)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** (0.5)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> float:
        scalar_product = self.x * other.x + self.y * other.y
        cos_a = scalar_product / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        other1 = Vector(0, 1)
        return round(self.angle_between(other1))

    def rotate(self, degrees: int) -> Vector:
        # x' = x*cos(α) — y*sin(α), y' = x*sin(α) + y*cos(α)
        degrees_rad = math.radians(degrees)
        x_rot = self.x * math.cos(degrees_rad) - self.y * math.sin(degrees_rad)
        y_rot = self.x * math.sin(degrees_rad) + self.y * math.cos(degrees_rad)
        return Vector(x_rot, y_rot)
