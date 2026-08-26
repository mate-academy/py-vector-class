from __future__ import annotations
import math


class Vector:
    def __init__(self, x_value: int | float, y_value: int | float) -> None:
        self.x = round(x_value, 2)
        self.y = round(y_value, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector:
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
        x_value = end_point[0] - start_point[0]
        y_value = end_point[1] - start_point[1]
        return cls(x_value, y_value)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def scalar_product(self, other: Vector) -> float:
        return self.x * other.x + self.y * other.y

    def angle_between(self, other: Vector) -> int:
        scalar = self.scalar_product(other)
        cos_a = scalar / (self.get_length() * other.get_length())
        return math.ceil(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        cos_angle = self.y / self.get_length()
        angle_rad = math.acos(cos_angle)
        angle_deg = math.degrees(angle_rad)
        return round(angle_deg)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        return Vector(
            round(self.x * math.cos(radians) - self.y * math.sin(radians), 2),
            round(self.x * math.sin(radians) + self.y * math.cos(radians), 2)
        )
