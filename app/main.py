from __future__ import annotations
import math


class Vector:
    def __init__(
            self,
            coordinate_of_x: float | int,
            coordinate_of_y: float | int
    ) -> None:
        self.x = round(coordinate_of_x, 2)
        self.y = round(coordinate_of_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            round(self.x + other.x, 2),
            round(self.y + other.y, 2)
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            round(self.x - other.x, 2),
            round(self.y - other.y, 2)
        )

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(
            round(self.x * other, 2),
            round(self.y * other, 2)
        )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            round(end_point[0] - start_point[0], 2),
            round(end_point[1] - start_point[1], 2)
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            round(self.x / self.get_length(), 2),
            round(self.y / self.get_length(), 2)
        )

    def angle_between(self, other: Vector) -> int:
        return round(math.degrees(math.acos(
            (self.x * other.x + self.y * other.y)
            / (self.get_length() * other.get_length())
        )))

    def get_angle(self) -> int:
        return abs(round(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, degrees: int) -> Vector:
        degrees = math.radians(degrees)
        cosine = math.cos(degrees)
        sinus = math.sin(degrees)
        return Vector(
            round(cosine * self.x - sinus * self.y, 2),
            round(sinus * self.x + cosine * self.y, 2)
        )
