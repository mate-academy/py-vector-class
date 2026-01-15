from __future__ import annotations
import math


class Vector:
    def __init__(self, x10: int | float, y10: int | float) -> None:
        self.x = round(x10, 2)
        self.y = round(y10, 2)

    def __add__(self, other: int | float | Vector) -> int | float | Vector:
        return Vector(round(self.x + other.x, 2), round(self.y + other.y, 2))

    def __sub__(self, other: int | float | Vector) -> int | float | Vector:
        return Vector(round(self.x - other.x, 2), round(self.y - other.y, 2))

    def __mul__(self, other: int | float | Vector) -> int | float | Vector:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

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

    def get_length(self) -> int | float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        scalar_product = self * other
        mods_product = self.get_length() * other.get_length()
        cos = scalar_product / mods_product
        return round(math.degrees(math.acos(cos)))

    def get_angle(self) -> int | float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        angle_rad = math.radians(degrees)
        new_x = self.x * math.cos(angle_rad) - self.y * math.sin(angle_rad)
        new_y = self.x * math.sin(angle_rad) + self.y * math.cos(angle_rad)
        return Vector(new_x, new_y)
