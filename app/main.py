from __future__ import annotations
import math


class Vector:
    def __init__(self, x_pt: float, y_pt: float) -> None:
        self.x_pt = round(x_pt, 2)
        self.y_pt = round(y_pt, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x_pt + other.x_pt, self.y_pt + other.y_pt)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x_pt - other.x_pt, self.y_pt - other.y_pt)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(self.x_pt * other, self.y_pt * other)
        else:
            return self.x_pt * other.x_pt + self.y_pt * other.y_pt

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
        return (self.x_pt ** 2 + self.y_pt ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x_pt / length, self.y_pt / length)

    def angle_between(self, other: Vector) -> float:
        angle = self * other / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(angle)))

    def get_angle(self) -> float:
        other = Vector(0, abs(self.y_pt))
        return self.angle_between(other)

    def rotate(self, degrees: float) -> Vector:
        angle = math.radians(degrees)
        x_pt = self.x_pt * math.cos(angle) - self.y_pt * math.sin(angle)
        y_pt = self.x_pt * math.sin(angle) + self.y_pt * math.cos(angle)
        return Vector(x_pt, y_pt)
