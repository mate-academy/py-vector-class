from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: int | float, y_coord: int | float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x_coord=self.x + other.x,
            y_coord=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x_coord=self.x - other.x,
            y_coord=self.y - other.y
        )

    def __mul__(self, other: int | Vector) -> Vector | int | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(
            x_coord=self.x * other,
            y_coord=self.y * other
        )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple) -> Vector:
        return cls(
            x_coord=end_point[0] - start_point[0],
            y_coord=end_point[1] - start_point[1]
        )

    def get_length(self) -> float | int:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            x_coord=round(self.x / self.get_length(), 2),
            y_coord=round(self.y / self.get_length(), 2)
        )

    def angle_between(self, vector: Vector) -> int:
        cos_a = (self * vector) / (((self.x ** 2 + self.y ** 2) ** 0.5)
                                   * ((vector.x ** 2 + vector.y ** 2) ** 0.5))
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        sin_a = self.y / self.get_length()
        return round(math.degrees(math.acos(sin_a)))

    def rotate(self, degrees: int) -> Vector:
        angle = degrees
        return Vector(
            x_coord=self.x * math.cos(math.radians(angle))
            - self.y * math.sin(math.radians(angle)),
            y_coord=self.x * math.sin(math.radians(angle))
            + self.y * math.cos(math.radians(angle))
        )
