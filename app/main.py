from __future__ import annotations
from math import sin, cos, acos, degrees, radians


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if (isinstance(other, float) or (isinstance(other, int))):
            return Vector(
                round(self.x * other, 2),
                round(self.y * other, 2)
            )
        else:
            return self.x * other.x + self.y * other.y

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
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        vector_length_inversion = 1 / self.get_length()
        return Vector(
            round(self.x * vector_length_inversion, 2),
            round(self.y * vector_length_inversion, 2)
        )

    def get_angle(self) -> float:
        return round(degrees(acos(self.y / self.get_length())))

    def angle_between(self, vector: Vector) -> float:
        return round(
            degrees(
                acos(
                    (self * vector) / (self.get_length() * vector.get_length())
                )
            )
        )

    def rotate(self, degree: int) -> Vector:
        radian = radians(degree)
        return Vector(
            round(self.x * cos(radian) - self.y * sin(radian), 2),
            round(self.x * sin(radian) + self.y * cos(radian), 2)
        )
