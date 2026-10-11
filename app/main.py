from __future__ import annotations
from math import sqrt, degrees, acos, atan2, cos, sin, radians


class Vector:
    def __init__(self, coordinate_x: int, coordinate_y: int) -> None:
        self.x = round(coordinate_x, 2)
        self.y = round(coordinate_y, 2)

    def __add__(self, vector: Vector) -> Vector:
        return Vector(self.x + vector.x, self.y + vector.y)

    def __sub__(self, vector: Vector) -> Vector:
        return Vector(self.x - vector.x, self.y - vector.y)

    def __mul__(self, vector: Vector | int | float) -> Vector | int | float:
        if isinstance(vector, Vector):
            return (self.x * vector.x) + (self.y * vector.y)
        elif isinstance(vector, (int, float)):
            return Vector(self.x * vector, self.y * vector)

    def get_length(self) -> int | float:
        return sqrt((self.x ** 2) + (self.y ** 2))

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, vector: Vector) -> int | float:
        cos_a = (
            (self * vector)
            / (self.get_length() * vector.get_length())
        )
        angle_degrees = degrees(acos(cos_a))
        return round(angle_degrees)

    def get_angle(self) -> int:
        return round(abs(degrees(atan2(self.x, self.y))))

    def rotate(self, angle: int | float) -> Vector:
        angle = radians(angle)
        coordinate_x = self.x * cos(angle) - self.y * sin(angle)
        coordinate_y = self.x * sin(angle) + self.y * cos(angle)

        return Vector(coordinate_x, coordinate_y)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple(int | float),
            end_point: tuple(int | float)
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )
