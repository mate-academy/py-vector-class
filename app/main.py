from __future__ import annotations
import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other) -> Vector:
        if isinstance(self, Vector):
            return Vector(
                x=self.x + other.x,
                y=self.y + other.y
            )

    def __sub__(self, other) -> Vector:
        if isinstance(self, Vector):
            return Vector(
                x=self.x - other.x,
                y=self.y - other.y
            )

    def __mul__(self, other: Vector or float) -> Vector or float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple[float, float],
                                    end_point: tuple[float, float]) -> Vector:
        start_x, start_y = start_point
        end_x, end_y = end_point
        x = end_x - start_x
        y = end_y - start_y
        return cls(x, y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        cos_angle = dot_product / (self.get_length() * other.get_length())
        angle_in_radians = math.acos(cos_angle)
        angle_in_degrees = round(math.degrees(angle_in_radians))
        return angle_in_degrees

    def get_angle(self) -> int:
        reference_vector = Vector(0, 1)
        return self.angle_between(reference_vector)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(new_x, new_y)
