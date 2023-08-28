from __future__ import annotations
from math import cos, sin, acos, degrees, radians


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x_coord=self.x + other.x,
            y_coord=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x_coord=self.x - other.x,
            y_coord=self.y - other.y
        )

    def __mul__(self, other: float | int | Vector) -> Vector | float:
        if isinstance(other, (float, int)):
            return Vector(
                x_coord=self.x * other,
                y_coord=self.y * other
            )
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple
                                    ) -> Vector:
        return cls(
            x_coord=end_point[0] - start_point[0],
            y_coord=end_point[1] - start_point[1]
        )

    def get_length(self: Vector) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        result_length = self.get_length()
        return Vector(
            x_coord=self.x / result_length,
            y_coord=self.y / result_length
        )

    def angle_between(self, other: Vector) -> int:
        result = self.__mul__(other) / (self.get_length() * other.get_length())
        return round(degrees(acos(result)))

    def get_angle(self) -> int:
        other = Vector(x_coord=0, y_coord=100)
        return self.angle_between(other=other)

    def rotate(self, degree: int) -> Vector:
        cos_rad = cos(radians(degree))
        sin_rad = sin(radians(degree))
        return Vector(
            x_coord=cos_rad * self.x - sin_rad * self.y,
            y_coord=sin_rad * self.x + cos_rad * self.y
        )
