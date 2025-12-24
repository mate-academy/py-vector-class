from __future__ import annotations
import math


class Vector:
    def __init__(self, coordinate_x: float, coordinate_y: float) -> None:
        self.x = round(coordinate_x, 2)
        self.y = round(coordinate_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            coordinate_x=self.x + other.x,
            coordinate_y=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            coordinate_x=self.x - other.x,
            coordinate_y=self.y - other.y
        )

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(
            coordinate_x=self.x * other,
            coordinate_y=self.y * other
        )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            coordinate_x=end_point[0] - start_point[0],
            coordinate_y=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            coordinate_x=self.x / self.get_length(),
            coordinate_y=self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> int:
        return round(
            math.degrees(
                math.acos(
                    (self * other)
                    / (self.get_length()
                       * other.get_length())
                )
            )
        )

    def get_angle(self) -> int:
        return round(math.degrees(math.acos(self.y / self.get_length())))

    def rotate(self, degrees: float) -> Vector:
        radians = math.radians(degrees)
        sin_radians = math.sin(radians)
        cos_radians = math.cos(radians)
        return Vector(
            coordinate_x=self.x * cos_radians - self.y * sin_radians,
            coordinate_y=self.x * sin_radians + self.y * cos_radians
        )
