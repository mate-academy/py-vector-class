from __future__ import annotations
import math


class Vector:
    def __init__(self, x_cord: float, y_cord: float) -> None:
        self.x: float = round(x_cord, 2)
        self.y: float = round(y_cord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector or float) -> Vector or float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y  # Dot product
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple,
            end_point: tuple) -> Vector:
        x_cord = end_point[0] - start_point[0]
        y_cord = end_point[1] - start_point[1]
        return cls(x_cord, y_cord)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> float:
        dot_product = self * other
        lengths_product = self.get_length() * other.get_length()
        if lengths_product == 0:
            return 0
        cos_angle = dot_product / lengths_product
        cos_angle = max(min(cos_angle, 1), -1)
        angle = math.degrees(math.acos(cos_angle))
        return round(angle)

    def get_angle(self) -> float:
        vertical = Vector(0, 1)
        return self.angle_between(vertical)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return self.__class__(new_x, new_y)
