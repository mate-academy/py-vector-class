from __future__ import annotations
import math


class Vector:
    def __init__(self, x_dot: float, y_dot: float) -> None:
        self.x = round(x_dot, 2)
        self.y = round(y_dot, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        elif isinstance(other, (int, float)):
            new_x = round(self.x * other, 2)
            new_y = round(self.y * other, 2)
            return Vector(new_x, new_y)
        else:
            raise TypeError("Unsupported operand type")

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple) -> Vector:
        return cls(end[0] - start[0], end[1] - start[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> float:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)), 0)

    def get_angle(self) -> int | float:
        y_axis = Vector(0, 1)
        cos_a = (self * y_axis) / (self.get_length() * y_axis.get_length())
        return round(math.degrees(math.acos(cos_a)), 0)

    def rotate(self, angle: float) -> Vector:
        angle = math.radians(angle)
        new_x = (self.x * math.cos(angle) - self.y * math.sin(angle))
        new_y = (self.x * math.sin(angle) + self.y * math.cos(angle))
        return Vector(new_x, new_y)
