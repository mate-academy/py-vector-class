from __future__ import annotations
import math


class Vector:
    def __init__(self, x_axe: float, y_axe: float) -> None:
        self.x = round(x_axe, 2)
        self.y = round(y_axe, 2)

    def __add__(self, other: Vector) -> Vector:
        x_axe = self.x + other.x
        y_axe = self.y + other.y
        return Vector(x_axe, y_axe)

    def __sub__(self, other: Vector) -> Vector:
        x_axe = self.x - other.x
        y_axe = self.y - other.y
        return Vector(x_axe, y_axe)

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        self.x = round(self.x * other, 2)
        self.y = round(self.y * other, 2)
        return self

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        x_axe = end_point[0] - start_point[0]
        y_axe = end_point[1] - start_point[1]
        return cls(x_axe, y_axe)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        x_axe = round(self.x / self.get_length(), 2)
        y_axe = round(self.y / self.get_length(), 2)
        return Vector(x_axe, y_axe)

    def angle_between(self, other: Vector) -> float:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> float:
        cos_a = self.y / self.get_length()
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: int) -> Vector:
        angle = math.radians(degrees)
        x_axe = self.x * math.cos(angle) - self.y * math.sin(angle)
        y_axe = self.x * math.sin(angle) + self.y * math.cos(angle)
        return Vector(x_axe, y_axe)
