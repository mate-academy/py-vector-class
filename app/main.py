from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: int | float, y_coord: int | float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> int | Vector:
        if isinstance(other, Vector):
            result = (self.x * other.x) + (self.y * other.y)
            return result
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        new_x = end_point[0] - start_point[0]
        new_y = end_point[1] - start_point[1]
        return cls(new_x, new_y)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, vector: Vector) -> float:
        scalar_addition = self.x * vector.x + self.y * vector.y
        vector_modules = vector.get_length() * self.get_length()
        angle = math.degrees(math.acos(scalar_addition / vector_modules))
        return round(angle)

    def get_angle(self) -> float:
        angle = math.degrees(math.acos(self.y / self.get_length()))
        return round(angle)

    def rotate(self, angle: float) -> Vector:
        rad_angle = math.radians(angle)
        new_x = self.x * math.cos(rad_angle) - self.y * math.sin(rad_angle)
        new_y = self.x * math.sin(rad_angle) + self.y * math.cos(rad_angle)
        return Vector(new_x, new_y)
