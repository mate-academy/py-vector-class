from __future__ import annotations
from math import acos, cos, sin, degrees, radians


class Vector:
    def __init__(self, x_point: float, y_point: float) -> None:
        self.x = round(x_point, 2)
        self.y = round(y_point, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x_point=(self.x + other.x),
            y_point=(self.y + other.y)
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x_point=(self.x - other.x),
            y_point=(self.y - other.y)
        )

    def __mul__(
            self,
            other: Vector | float | int
    ) -> Vector | float:
        if isinstance(other, (float, int)):
            return Vector(
                x_point=(self.x * other),
                y_point=(self.y * other)
            )
        return ((self.x * other.x)
                + (self.y * other.y))

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return Vector(
            x_point=(end_point[0] - start_point[0]),
            y_point=(end_point[1] - start_point[1])
        )

    def get_length(self) -> float:
        return ((self.x ** 2)
                + (self.y ** 2)) ** 0.5

    def get_normalized(self) -> Vector:
        vector_length = self.get_length()
        return Vector(
            x_point=(self.x / vector_length),
            y_point=(self.y / vector_length)
        )

    def angle_between(self, other: Vector) -> int:
        vector_length1 = self.get_length()
        vector_length2 = other.get_length()
        vector_multiplication = self * other
        return round(
            degrees(
                acos(
                    vector_multiplication / (vector_length1 * vector_length2)
                )
            )
        )

    def get_angle(self) -> int:
        vector_length = round(self.get_length(), 2)
        if self.x:
            if self.y >= 0:
                return int(
                    degrees(
                        acos(
                            self.y / vector_length
                        )
                    )
                )
            else:
                return round(
                    degrees(
                        acos(
                            self.y / vector_length
                        )
                    )
                )
        return 0

    def rotate(self, number: int) -> Vector:
        x_number = ((self.x * cos(radians(number)))
                    - (self.y * sin(radians(number))))
        y_number = ((self.x * sin(radians(number)))
                    + (self.y * cos(radians(number))))
        return Vector(
            x_point=x_number,
            y_point=y_number
        )
