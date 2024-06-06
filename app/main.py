from __future__ import annotations
import math


class Vector:
    def __init__(self, x_cord: float, y_cord: float) -> None:
        self.x_cord = round(x_cord, 2)
        self.y_cord = round(y_cord, 2)

    def __add__(self, other: Vector) -> Vector:
        x_cord = self.x_cord + other.x_cord
        y_cord = self.y_cord + other.y_cord
        return Vector(x_cord, y_cord)

    def __sub__(self, other: Vector) -> Vector:
        x_cord = self.x_cord - other.x_cord
        y_cord = self.y_cord - other.y_cord
        return Vector(x_cord, y_cord)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector) is True:
            return self.x_cord * other.x_cord + self.y_cord * other.y_cord
        return Vector(self.x_cord * other, self.y_cord * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        start_x, start_y = start_point
        start_vector = Vector(start_x, start_y)

        end_x, end_y = end_point
        end_vector = Vector(end_x, end_y)

        return end_vector - start_vector

    def get_length(self) -> float:
        return (self.x_cord ** 2 + self.y_cord ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        x_cord = self.x_cord / length
        y_cord = self.y_cord / length
        return Vector(x_cord, y_cord)

    def angle_between(self, other: Vector) -> int:
        cos_a = self * other / (self.get_length() * other.get_length())
        angle = math.degrees(math.acos(cos_a))
        return round(angle)

    def get_angle(self) -> int:
        other = Vector(0, 1)
        return self.angle_between(other)

    def rotate(self, degrees: int) -> Vector:
        """rx = x cos α - y sin α  ry = y cos α + x sin α"""
        radians = math.radians(degrees)
        x_cord = (self.x_cord * math.cos(radians)
                  - self.y_cord * math.sin(radians))
        y_cord = (self.y_cord * math.cos(radians)
                  + self.x_cord * math.sin(radians))
        return Vector(x_cord, y_cord)
