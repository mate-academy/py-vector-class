from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
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

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(
            x_coordinate=self.x * other,
            y_coordinate=self.y * other
        )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            x_coordinate=end_point[0] - start_point[0],
            y_coordinate=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            x_coordinate=self.x / self.get_length(),
            y_coordinate=self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> int:
        mul_vectors = self.__mul__(other)
        mul_lengths = self.get_length() * other.get_length()
        return round(math.degrees(math.acos(mul_vectors / mul_lengths)))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, abs(self.y)))

    def rotate(self, degrees: int) -> Vector:
        degrees = math.radians(degrees)
        return Vector(
            x_coordinate=self.x * math.cos(degrees) - (
                self.y * math.sin(degrees)),
            y_coordinate=self.x * math.sin(degrees) + (
                self.y * math.cos(degrees))
        )
