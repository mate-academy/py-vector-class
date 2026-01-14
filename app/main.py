from __future__ import annotations
import math


class Vector:
    def __init__(self, ox: int | float, oy: int | float) -> None:
        self.x = round(ox, 2)
        self.y = round(oy, 2)

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

    def __mul__(self, other: Vector | float | int) -> Vector:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector(round((self.x * other), 2), round((self.y * other), 2))

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple(float),
            end_point: tuple(float)
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> float:
        if self.get_length() == 0:
            return Vector(0, 0)
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        length = self.x * other.x + self.y * other.y
        cosine = length / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cosine)))

    def get_angle(self) -> int:
        positive_y = Vector(0, 1)
        return self.angle_between(positive_y)

    def rotate(self, angle: int) -> Vector:
        rad = math.radians(angle)
        rotated_x = self.x * math.cos(rad) - self.y * math.sin(rad)
        rotated_y = self.x * math.sin(rad) + self.y * math.cos(rad)
        return Vector(rotated_x, rotated_y)
