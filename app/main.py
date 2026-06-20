from __future__ import annotations
import math


class Vector:
    def __init__(self, point_x: int | float, point_y: int | float) -> None:
        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

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

    def __mul__(self, other: int | float | Vector) -> int | float | Vector:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple[int | float, int | float],
        end_point: tuple[int | float, int | float],
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> int | float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        vector_length = self.get_length()
        return Vector(
            self.x / vector_length, self.y / vector_length
        )

    def angle_between(self, other: Vector) -> int:
        angle_cos = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(angle_cos)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        cosinus = math.cos(math.radians(degrees))
        sinus = math.sin(math.radians(degrees))
        return Vector(
            self.x * cosinus - self.y * sinus,
            self.x * sinus + self.y * cosinus,
        )
