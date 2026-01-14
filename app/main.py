from __future__ import annotations
import math


class Vector:
    def __init__(self, coordinate_x: float, coordinate_y: float) -> None:
        self.x = round(coordinate_x, 2)
        self.y = round(coordinate_y, 2)

    def __add__(self, other: int | float) -> Vector:
        if isinstance(other, Vector):
            return Vector(
                coordinate_x=self.x + other.x,
                coordinate_y=self.y + other.y
            )

    def __sub__(self, other: int | float) -> Vector:
        if isinstance(other, Vector):
            return Vector(
                coordinate_x=self.x - other.x,
                coordinate_y=self.y - other.y
            )

    def __mul__(self, other: Vector | float | int) -> Vector | int | float:
        if not isinstance(other, Vector):
            return Vector(
                coordinate_x=round(self.x * other, 2),
                coordinate_y=round(self.y * other, 2)
            )
        return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return Vector(
            coordinate_x=end_point[0] - start_point[0],
            coordinate_y=end_point[1] - start_point[1]
        )

    def get_length(self) -> int | float:
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(
            coordinate_x=self.x / length,
            coordinate_y=self.y / length
        )

    def angle_between(self, other: Vector) -> int:
        cos_of_angle = ((self * other)
                        / (self.get_length()
                           * other.get_length()))
        angle_in_radians = math.acos(cos_of_angle)
        angle_in_degrees = round(math.degrees(angle_in_radians))
        return angle_in_degrees

    def get_angle(self) -> int | float:
        angle_in_radians = math.atan2(self.x, self.y)
        angle_in_degrees = round(math.degrees(angle_in_radians))
        return abs(angle_in_degrees)

    def rotate(self, degree: int) -> Vector:
        radians = math.radians(degree)
        return Vector(
            self.x * math.cos(radians) - self.y * math.sin(radians),
            self.y * math.cos(radians) + self.x * math.sin(radians)
        )
