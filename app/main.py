from __future__ import annotations
from math import acos, degrees, radians, cos, sin


class Vector:
    def __init__(self, x_coord: int, y_coord: int) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        else:
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(
            end_point[0] - start_point[0], end_point[1] - start_point[1]
        )

    def get_length(self) -> None:
        return (self.x**2 + self.y**2)**0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(round(self.x / length, 2),
                      round(self.y / length, 2))

    def angle_between(self, other: Vector) -> int:
        dot_product = self.__mul__(other)
        magnitude_1, magnitude_2 = self.get_length(), other.get_length()
        return round(degrees(acos(dot_product / (magnitude_1 * magnitude_2))))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degree: int) -> Vector:
        angle_radians = radians(degree)

        x_rotated = (self.x * cos(angle_radians)
                     - self.y * sin(angle_radians))
        y_rotated = (self.x * sin(angle_radians)
                     + self.y * cos(angle_radians))

        return Vector(x_rotated, y_rotated)
