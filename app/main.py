from __future__ import annotations
import math


class Vector:
    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[float, float],
            end_point: tuple[float, float]
    ) -> Vector:
        start_x, start_y = start_point
        end_x, end_y = end_point
        new_x = end_x - start_x
        new_y = end_y - start_y
        return cls(new_x, new_y)

    def __init__(self, x_value: int | float, y_value: int | float) -> None:
        self.x = round(x_value, 2)
        self.y = round(y_value, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> float | Vector:
        if isinstance(other, Vector):
            return self.get_dot_product(other)
        return Vector(round(self.x * other, 2), round(self.y * other, 2))

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        vector_length = self.get_length()
        if vector_length == 0:
            return Vector(0, 0)
        return Vector(
            round(self.x / vector_length, 2),
            round(self.y / vector_length, 2)
        )

    def angle_between(self, other: Vector) -> int | float:
        dot_product = self.get_dot_product(other)
        length_self = self.get_length()
        length_other = other.get_length()

        cos_a = dot_product / (length_self * length_other)
        angle_rad = math.acos(cos_a)
        angle_deg = math.degrees(angle_rad)

        return round(angle_deg)

    def get_angle(self) -> int | float:
        return self.angle_between(Vector(0, 10))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)

        new_x = (self.x * math.cos(radians) - self.y * math.sin(radians))
        new_y = (self.x * math.sin(radians) + self.y * math.cos(radians))

        return Vector(round(new_x, 2), round(new_y, 2))

    def get_dot_product(self, other: Vector) -> float:
        return self.x * other.x + self.y * other.y
