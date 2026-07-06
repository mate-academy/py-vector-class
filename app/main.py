from __future__ import annotations
import math


class Vector:
    def __init__(self, variable_1: float, variable_2: float) -> None:
        self.x = round(variable_1, 2)
        self.y = round(variable_2, 2)

    def __add__(self, other: Vector) -> Vector:
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __sub__(self, other: Vector) -> Vector:
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def get_normalized(self) -> Vector:
        divider = self.get_length()
        if divider == 0:
            return Vector(0, 0)
        return Vector(self.x / divider, self.y / divider)

    def angle_between(self, other: Vector) -> int:
        cos_a = ((self * other) / (self.get_length() * other.get_length()))
        return int(round(math.degrees(math.acos(cos_a))))

    def get_angle(self) -> int:
        cos_a = self.y / self.get_length()
        return int(round(math.degrees(math.acos(cos_a))))

    def rotate(self, angle: int) -> Vector:
        new_x = (self.x * math.cos(math.radians(angle))
                 - self.y * math.sin(math.radians(angle)))
        new_y = (self.x * math.sin(math.radians(angle))
                 + self.y * math.cos(math.radians(angle)))
        return Vector(new_x, new_y)
