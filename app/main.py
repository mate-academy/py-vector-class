from __future__ import annotations
import math


class Vector:
    def __init__(
            self,
            first_coordinate: float,
            second_coordinate: float
    ) -> None:
        self.x = round(first_coordinate, 2)
        self.y = round(second_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, other: float | Vector) -> Vector | float:
        if isinstance(other, float | int):
            return Vector(
                self.x * other,
                self.y * other
            )
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        first_coordinate = end_point[0] - start_point[0]
        second_coordinate = end_point[1] - start_point[1]
        return cls(
            first_coordinate,
            second_coordinate
        )

    def get_length(self) -> float:
        return (self.x**2 + self.y**2)**0.5

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / Vector.get_length(self),
            self.y / Vector.get_length(self)
        )

    def angle_between(self, other: Vector) -> int:
        dot_product = self.x * other.x + self.y * other.y
        magnitude_self = self.get_length()
        magnitude_other = other.get_length()
        cos_result = dot_product / (magnitude_self * magnitude_other)
        radians = math.acos(cos_result)
        degrees = round(math.degrees(radians))
        return degrees

    def get_angle(self) -> int:
        radians = math.atan2(self.x, self.y)
        degrees = round(math.degrees(radians))
        return abs(degrees)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        first_coordinate = (math.cos(radians) * self.x
                            - math.sin(radians) * self.y)
        second_coordinate = (math.sin(radians) * self.x
                             + math.cos(radians) * self.y)
        return Vector(
            first_coordinate,
            second_coordinate
        )
