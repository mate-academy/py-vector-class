from __future__ import annotations
from math import acos, degrees, cos, sin, radians


class Vector:
    def __init__(self, x_coordinates: float, y_coordinates: float) -> None:
        self.x = round(x_coordinates, 2)
        self.y = round(y_coordinates, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        final = None

        if isinstance(other, Vector):
            final = self.x * other.x + self.y * other.y
        else:
            final = Vector(self.x * other, self.y * other)

        return final

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> int | float:
        return (self.x**2 + self.y**2)**0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()

        return Vector(self.x / length, self.y / length)

    def angle_between(self, vector: Vector) -> int:
        return round(
            degrees(
                acos(
                    (self * vector) / (self.get_length() * vector.get_length())
                )
            )
        )

    def get_angle(self) -> int | float:
        return self.angle_between((Vector(0, 1)))

    def rotate(self, degree: int) -> Vector:
        cs = cos(radians(degree))
        sn = sin(radians(degree))

        return Vector(
            cs * self.x - sn * self.y,
            sn * self.x + cs * self.y
        )
