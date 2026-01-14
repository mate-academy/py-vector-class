from __future__ import annotations
import math


class Vector:

    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: Vector) -> Vector:
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __sub__(self, other: Vector) -> Vector:
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)

    def __mul__(self, other: Vector | int | float) -> Vector:
        if isinstance(other, (int, float)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        new_x = end_point[0] - start_point[0]
        new_y = end_point[1] - start_point[1]
        return cls(new_x, new_y)

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        lenght = self.get_length()
        return Vector(self.x / lenght, self.y / lenght)

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        lenght_product = self.get_length() * other.get_length()
        cos_thet = dot_product / lenght_product
        cos_thet = max(-1, min(1, cos_thet))
        angle = math.degrees(math.acos(cos_thet))
        return round(angle)

    def get_angle(self) -> float:
        dot_product = self.y * 1
        lenght_product = self.get_length()

        cos_thet = dot_product / lenght_product
        cos_thet = max(-1, min(1, cos_thet))
        angle = math.degrees(math.acos(cos_thet))
        return round(angle)

    def rotate(self, degrees: int) -> Vector:
        rad = math.radians(degrees)
        new_x = self.x * math.cos(rad) - self.y * math.sin(rad)
        new_y = self.x * math.sin(rad) + self.y * math.cos(rad)

        return Vector(new_x, new_y)
