from __future__ import annotations
import math


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x,
                          self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x,
                          self.y - other.y)

    def __mul__(self, other: Vector) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        coord_x = round(end_point[0] - start_point[0], 2)
        coord_y = round(end_point[1] - start_point[1], 2)
        return cls(coord_x, coord_y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        dot_product = self * other
        cos_a = dot_product / (self.get_length() * other.get_length())
        angle_rad = math.acos(cos_a)
        angle_deg = round(math.degrees(angle_rad))
        return angle_deg

    def get_angle(self) -> int:
        reference_vector = Vector(0, 1)
        return self.angle_between(reference_vector)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        new_x = (self.x * math.cos(radians)
                 - self.y * math.sin(radians))
        new_y = (self.x * math.sin(radians)
                 + self.y * math.cos(radians))
        return Vector(new_x, new_y)
