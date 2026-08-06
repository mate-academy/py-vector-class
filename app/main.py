from __future__ import annotations
import math


class Vector:
    def __init__(self, x_value: float, y_value: float) -> None:
        self.x = round(x_value, 2)
        self.y = round(y_value, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        else:
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> float:
        angle = self * other / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(angle)))

    def get_angle(self) -> float:
        other = Vector(0, abs(self.y))
        return self.angle_between(other)

    def rotate(self, degrees: float) -> Vector:
        angle = math.radians(degrees)
        x_pt = self.x * math.cos(angle) - self.y * math.sin(angle)
        y_pt = self.x * math.sin(angle) + self.y * math.cos(angle)
        return Vector(x_pt, y_pt)
