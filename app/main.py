from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        dot = self * other
        len1 = self.get_length()
        len2 = other.get_length()
        cos_a = dot / (len1 * len2)
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return abs(round(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, degrees: int) -> Vector:
        new_x = (
            self.x
            * math.cos(math.radians(degrees))
            - self.y * math.sin(math.radians(degrees))
        )
        new_y = (
            self.x
            * math.sin(math.radians(degrees))
            + self.y * math.cos(math.radians(degrees))
        )
        return Vector(new_x, new_y)
