from __future__ import annotations
import math


class Vector:
    def __init__(
            self,
            x_coordinate: float | int,
            y_coordinate: float | int
    ) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x_coordinate=self.x + other.x,
            y_coordinate=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x_coordinate=self.x - other.x,
            y_coordinate=self.y - other.y
        )

    def __mul__(self, other: int | float | Vector) -> Vector | int | float:
        if isinstance(other, (int, float)):
            return Vector(
                x_coordinate=self.x * other,
                y_coordinate=self.y * other
            )
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        return cls(
            x_coordinate=end_point[0] - start_point[0],
            y_coordinate=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        magnitude = self.get_length()
        return Vector(
            x_coordinate=self.x / magnitude,
            y_coordinate=self.y / magnitude
        )

    def angle_between(self, other: Vector) -> int:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return int(round(math.degrees(math.acos(cos_a)), 0))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        sin = math.sin(radians)
        cos = math.cos(radians)
        return Vector(
            x_coordinate=self.x * cos - self.y * sin,
            y_coordinate=self.x * sin + self.y * cos
        )
