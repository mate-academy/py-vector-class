from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            round(self.x + other.x, 2),
            round(self.y + other.y, 2),
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            round(self.x - other.x, 2),
            round(self.y - other.y, 2),
        )

    def __mul__(self, other: float | Vector) -> float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(
            round(self.x * other, 2),
            round(self.y * other, 2),
        )

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple[float, float], end_point: tuple[float, float]
    ) -> Vector:
        x_coordinate = round(end_point[0] - start_point[0], 2)
        y_coordinate = round(end_point[1] - start_point[1], 2)
        return cls(x_coordinate, y_coordinate)

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(
            round(self.x / length, 2),
            round(self.y / length, 2),
        )

    def angle_between(self, other: Vector) -> int:
        if self.get_length() == 0 or other.get_length() == 0:
            raise ValueError("Cannot calculate angle with zero-length vector")
        cos_a = (self.x * other.x + self.y * other.y) / (
            self.get_length() * other.get_length()
        )
        angle = math.degrees(math.acos(max(-1, min(1, cos_a))))
        return round(angle)

    def get_angle(self) -> int:
        positive_y = Vector(0, 1)
        return self.angle_between(positive_y)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        x_rotated = self.x * math.cos(radians) - self.y * math.sin(radians)
        y_rotated = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(round(x_rotated, 2), round(y_rotated, 2))
