from __future__ import annotations
import math


class Vector:
    def __init__(self, point_x: float, point_y: float) -> None:
        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: int | float | Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        point_x = end_point[0] - start_point[0]
        point_y = end_point[1] - start_point[1]
        return cls(point_x, point_y)

    def get_length(self) -> int | float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        return round(
            math.degrees(
                math.acos(
                    Vector.__mul__(self, other)
                    / (self.get_length() * other.get_length())
                )
            )
        )

    def get_angle(self) -> int | float:
        return self.angle_between(Vector(0, abs(self.y)))

    def rotate(self, angle: int) -> Vector:
        radians = math.radians(angle)
        x1 = self.x * math.cos(radians) - self.y * math.sin(radians)
        y1 = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(x1, y1)
