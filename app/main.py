from __future__ import annotations
import math


class Vector:
    def __init__(self, x_pos: int | float = 0, y_pos: int | float = 0) -> None:
        self.x = round(x_pos, 2)
        self.y = round(y_pos, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(cls,
                                    point1: tuple[int | float,
                                                  int | float],
                                    point2: tuple[int | float,
                                                  int | float]) -> Vector:
        return cls(point2[0] - point1[0], point2[1] - point1[1])

    def get_length(self) -> float:
        return math.hypot(self.x, self.y)

    def get_normalized(self) -> Vector:
        magnitude = self.get_length()
        return Vector(self.x / magnitude, self.y / magnitude)

    def angle_between(self, other: Vector) -> float:
        dot_product = self * other
        magnitude_self = self.get_length()
        magnitude_other = other.get_length()
        cos_angle = dot_product / (magnitude_self * magnitude_other)
        return round(math.degrees(math.acos(cos_angle)))

    def get_angle(self) -> float:
        return round(math.degrees(math.acos(self.y / self.get_length())))

    def rotate(self, angle: float) -> Vector:
        x_cos_angle = math.cos(math.radians(angle))
        y_sin_angle = math.sin(math.radians(angle))
        new_x = self.x * x_cos_angle - self.y * y_sin_angle
        new_y = self.x * y_sin_angle + self.y * x_cos_angle
        return Vector(new_x, new_y)
