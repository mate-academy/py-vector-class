from __future__ import annotations
import math


class Vector:

    def __init__(self, point_x: float, point_y: float) -> None:
        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple,
            end_point: tuple
    ) -> Vector:
        vector = (end_point[0] - start_point[0], end_point[1] - start_point[1])
        return cls(vector[0], vector[1])

    def get_length(self) -> float:
        return math.sqrt((self.x ** 2 + self.y ** 2))

    def get_normalized(self) -> Vector:
        length = self.get_length()
        new_x = self.x / length
        new_y = self.y / length
        return Vector(new_x, new_y)

    def angle_between(self, other: Vector) -> int:
        arc_cosine_value = math.acos(
            (self * other) / (self.get_length() * other.get_length())
        )
        return round(math.degrees(arc_cosine_value))

    def get_angle(self) -> int:
        angle_radians = math.atan2(self.x, self.y)
        angle_degrees = math.degrees(angle_radians)
        return abs(round(angle_degrees))

    def rotate(self, angle: int | float) -> Vector:
        angle = math.radians(angle)
        new_x_degrees = self.x * math.cos(angle) - self.y * math.sin(angle)
        new_y_degrees = self.x * math.sin(angle) + self.y * math.cos(angle)
        new_x = round(new_x_degrees, 2)
        new_y = round(new_y_degrees, 2)
        return Vector(new_x, new_y)
