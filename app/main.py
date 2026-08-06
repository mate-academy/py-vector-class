from __future__ import annotations
from math import sqrt, acos, cos, sin, radians, degrees


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple(float, float),
        end_point: tuple(float, float)
    ) -> Vector:
        return cls(
            x_coordinate=end_point[0] - start_point[0],
            y_coordinate=end_point[1] - start_point[1]
        )

    def __add__(self, vector2: Vector) -> Vector:
        return Vector(
            x_coordinate=self.x + vector2.x,
            y_coordinate=self.y + vector2.y
        )

    def __sub__(self, vector2: Vector) -> Vector:
        return Vector(
            x_coordinate=self.x - vector2.x,
            y_coordinate=self.y - vector2.y
        )

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(
            x_coordinate=self.x * other,
            y_coordinate=self.y * other
        )

    def get_length(self) -> float:
        return sqrt(abs(self.x) ** 2 + abs(self.y) ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            x_coordinate=self.x / self.get_length(),
            y_coordinate=self.y / self.get_length()
        )

    def angle_between(self, vector2: Vector) -> int:
        cos_a = (self * vector2) / (self.get_length() * vector2.get_length())

        return round(degrees(acos(cos_a)))

    def get_angle(self) -> int:
        cos_a = self.y / self.get_length()

        return round(degrees(acos(cos_a)))

    def rotate(self, angle: int) -> Vector:
        rad = radians(angle)
        cos_a = cos(rad)
        sin_a = sin(rad)

        return Vector(
            x_coordinate=cos_a * self.x - sin_a * self.y,
            y_coordinate=sin_a * self.x + cos_a * self.y
        )
