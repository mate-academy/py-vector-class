from __future__ import annotations
import math


class Vector:
    def __init__(self, xcoordinate: float, ycoordinate: float) -> None:
        self.x = round(xcoordinate, 2)
        self.y = round(ycoordinate, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple)\
            -> "Vector":
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> "Vector":
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: "Vector") -> float:
        dot = self.x * other.x + self.y * other.y
        cos_a = dot / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        cos_a = self.y / self.get_length()
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: float) -> "Vector":
        radians = math.radians(degrees)

        xcoordinate = self.x * math.cos(radians) - self.y * math.sin(radians)
        ycoordinate = self.x * math.sin(radians) + self.y * math.cos(radians)

        return Vector(round(xcoordinate, 2), round(ycoordinate, 2))
