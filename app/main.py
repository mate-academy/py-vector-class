from __future__ import annotations
import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other) -> object:
        if isinstance(other, Vector):
            return Vector(
                x=self.x + other.x,
                y=self.y + other.y
            )

    def __sub__(self, other) -> object:
        if isinstance(other, Vector):
            return Vector(
                x=self.x - other.x,
                y=self.y - other.y
            )

    def __mul__(self, other) -> object:
        if isinstance(other, Vector):

            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):

            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: float) -> int:
        cos = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos)))

    def get_angle(self) -> float:
        reference_vector = Vector(0, 1)
        return self.angle_between(reference_vector)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        x = round(self.x * math.cos(radians) - self.y * math.sin(radians), 2)
        y = round(self.x * math.sin(radians) + self.y * math.cos(radians), 2)
        return Vector(x, y)
