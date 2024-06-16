from __future__ import annotations
from math import dist, sqrt, acos, degrees, cos, sin, radians


class Vector:
    def __init__(self, coord_x: int | float, coord_y: int | float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(
                round(self.x + other.x, 2),
                round(self.y + other.y, 2)
            )

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(
                round(self.x - other.x, 2),
                round(self.y - other.y, 2)
            )

    def __mul__(self, other: Vector | int | float) -> Vector | float | int:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector(round(self.x * other, 2), round(self.y * other, 2))

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple) -> Vector:
        return cls(round(end[0] - start[0], 2), round(end[1] - start[1], 2))

    def get_length(self) -> float:
        return dist([0, 0], [self.x, self.y])

    def get_normalized(self) -> Vector:
        vector_length = self.get_length()
        return Vector(
            round(self.x / vector_length, 2),
            round(self.y / vector_length, 2)
        )

    def angle_between(self, vector: Vector) -> int:
        multiply = self.__mul__(vector)
        mod_vector_x = sqrt(self.x ** 2 + self.y ** 2)
        mod_vector_y = sqrt(vector.x ** 2 + vector.y ** 2)
        return round(degrees(acos(multiply / (mod_vector_x * mod_vector_y))))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, angle: int) -> Vector:
        radians_angle = radians(angle)
        rotate_x = self.x * cos(radians_angle) - self.y * sin(radians_angle)
        rotate_y = self.x * sin(radians_angle) + self.y * cos(radians_angle)
        return Vector(round(rotate_x, 2), round(rotate_y, 2))
