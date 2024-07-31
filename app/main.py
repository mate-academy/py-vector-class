from __future__ import annotations
from math import acos, radians, cos, sin, sqrt, degrees


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector((self.x + other.x), (self.y + other.y))

    def __sub__(self, other: Vector) -> Vector:
        return Vector((self.x - other.x), (self.y - other.y))

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector((self.x * other), (self.y * other))

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[float],
            end_point: tuple[float]
    ) -> Vector:
        return cls(
            (end_point[0] - start_point[0]),
            (end_point[1] - start_point[1])
        )

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            (self.x / self.get_length()),
            (self.y / self.get_length())
        )

    def angle_between(self, vector: Vector) -> int:
        dot_product = self * vector
        length = self.get_length() * vector.get_length()
        return round(degrees(acos(dot_product / length)))

    def get_angle(self) -> int:
        vector = Vector(0, 1)
        return round(self.angle_between(vector))

    def rotate(self, degree: int) -> Vector:
        angle_radians = radians(degree)

        cos_angle = cos(angle_radians)
        sin_angle = sin(angle_radians)

        x_coord = self.x * cos_angle - self.y * sin_angle
        y_coord = self.x * sin_angle + self.y * cos_angle

        return Vector(x_coord, y_coord)
