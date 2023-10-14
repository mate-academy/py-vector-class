from __future__ import annotations
import math


class Vector:
    def __init__(self, x_point: float, y_point: float) -> None:
        self.x_point = round(x_point, 2)
        self.y_point = round(y_point, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.x_point + other.x_point,
            self.y_point + other.y_point
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x_point - other.x_point,
            self.y_point - other.y_point
        )

    def __mul__(self, other: Vector | float | int) -> Vector | float:
        if type(other) == float or type(other) == int:
            return Vector(
                self.x_point * other,
                self.y_point * other
            )
        else:
            return (
                self.x_point * other.x_point
                + self.y_point * other.y_point
            )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[float],
            end_point: tuple[float]
    ) -> Vector:

        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x_point ** 2 + self.y_point ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            self.x_point / self.get_length(),
            self.y_point / self.get_length()
        )

    def angle_between(self, other: Vector) -> int:
        return round(
            math.degrees(
                math.acos(
                    (self * other) / (self.get_length() * other.get_length())
                )
            )
        )

    def get_angle(self) -> int:
        angle = math.degrees(math.atan2(self.x_point, self.y_point))
        return abs(round(angle))

    def rotate(self, degrees: int) -> Vector:
        rad = math.radians(degrees)
        cos_rad = math.cos(rad)
        sin_rad = math.sin(rad)
        x_point = self.x_point * cos_rad - self.y_point * sin_rad
        y_point = self.x_point * sin_rad + self.y_point * cos_rad
        return Vector(x_point, y_point)
