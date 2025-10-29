from __future__ import annotations
import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)


    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, float | int):
            return Vector(self.x * other, self.y * other)
        return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        x = end_point[0] - start_point[0]
        y = end_point[1] - start_point[1]
        return cls(x, y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self):
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> float | int:
        length_a = self.get_length()
        length_b = other.get_length()

        if length_a == 0 or length_b == 0:
            return 0.0

        cos_angle = (self * other) / (length_a * length_b)
        clamped_cos_angle = max(-1.0, min(1.0, cos_angle))
        angle_in_radians = math.acos(clamped_cos_angle)
        angle_in_degrees = math.degrees(angle_in_radians)
        return int(round(angle_in_degrees))

    def get_angle(self) -> float:
        positive_y_axis = Vector(0, 1)
        return self.angle_between(positive_y_axis)
    
    def rotate(self, degrees: float | int) -> Vector:
        radians = math.radians(degrees)
        cos_angle = math.cos(radians)
        sin_angle = math.sin(radians)
        new_x = self.x * cos_angle - self.y * sin_angle
        new_y = self.x * sin_angle + self.y * cos_angle
        return Vector(new_x, new_y)