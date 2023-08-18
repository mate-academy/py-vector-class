from __future__ import annotations
from math import sqrt, acos, degrees, atan2, sin, cos, radians


class Vector:
    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            coord_x=self.x + other.x,
            coord_y=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            coord_x=self.x - other.x,
            coord_y=self.y - other.y
        )

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple | Vector,
            end_point: tuple | Vector
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0], end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        vector_len = self.get_length()
        if vector_len != 0:
            norm_x = self.x / vector_len
            norm_y = self.y / vector_len
            return Vector(norm_x, norm_y)

    def angle_between(self, other_vector: Vector) -> int:
        first_angle = (self.x * other_vector.x + self.y * other_vector.y)
        second_angle = (self.get_length() * other_vector.get_length())
        angle_rad = acos(first_angle / second_angle)
        angle_degree = degrees(angle_rad)
        return round(angle_degree)

    def get_angle(self) -> int:
        return round(abs(degrees(atan2(self.x, self.y))))

    def rotate(self, degree: int) -> Vector:
        rad = radians(degree)
        rotate_x = self.x * cos(rad) - self.y * sin(rad)
        rotate_y = self.x * sin(rad) + self.y * cos(rad)
        return Vector(rotate_x, rotate_y)
