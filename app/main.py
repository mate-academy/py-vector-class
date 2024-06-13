from __future__ import annotations
import math


class Vector:
    def __init__(self, x: int | float, y: int | float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            round(self.x + other.x, 2),
            round(self.y + other.y, 2)
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            round(self.x - other.x, 2),
            round(self.y - other.y, 2)
        )

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(
                round(self.x * other, 2),
                round(self.y * other, 2)
            )
        return self.x * other.x + self.y + other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[int, int],
            end_point: tuple[int, int]
    ) -> Vector:
        return cls(
            round(end_point[0] - start_point[0], 2),
            round(end_point[1] - start_point[1], 2)
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        vector_norm = math.sqrt(self.x ** 2 + self.y ** 2)
        return Vector(
            round(self.x / vector_norm, 2),
            round(self.y / vector_norm, 2)
        )

    def angle_between(self, other: Vector) -> int:
        dot_product = self.x * other.x + self.y * other.y
        magnitude = self.get_length() * other.get_length()
        return round(math.degrees(math.acos(dot_product / magnitude)))

    def get_angle(self) -> int:
        dot_product = self.x * 0 + self.y * 1
        magnitude = self.get_length() * math.sqrt(0 ** 2 + 1 ** 2)
        return round(math.degrees(math.acos(dot_product / magnitude)))

    def rotate(self, degrees: int) -> Vector:
        x = self.x * math.cos(math.radians(degrees)) - self.y * math.sin(math.radians(degrees))
        y = self.x * math.sin(math.radians(degrees)) + self.y * math.cos(math.radians(degrees))
        return Vector(round(x, 2), round(y, 2))
