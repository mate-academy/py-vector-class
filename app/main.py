from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: "Vector" | float) -> "Vector" | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple) -> "Vector":
        return cls(x_coord=end[0] - start[0], y_coord=end[1] - start[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: "Vector") -> int:
        cos = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos)))

    def get_angle(self) -> int:
        result = round(math.degrees(math.atan2(self.x, self.y)))
        return abs(result)

    def rotate(self, other: int) -> "Vector":
        rad = math.radians(other)
        return Vector(
            x_coord=self.x * math.cos(rad) - self.y * math.sin(rad),
            y_coord=self.x * math.sin(rad) + self.y * math.cos(rad)
        )
