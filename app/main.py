from __future__ import annotations

import math


class Vector:
    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return Vector(round(end_point[0] - start_point[0], 2),
                      round(end_point[1] - start_point[1], 2))

    def __init__(self,
                 x_coordinate: float | int,
                 y_coordinate: float | int) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(round(self.x + other.x, 2),
                      round(self.y + other.y, 2))

    def __sub__(self, other: Vector) -> Vector:
        return Vector(round(self.x - other.x, 2),
                      round(self.y - other.y, 2))

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(round(self.x * other, 2), round(self.y * other, 2))

    def get_length(self) -> float | int:
        return (self.x ** 2 + self.y ** 2) ** (1 / 2)

    def get_normalized(self) -> Vector:
        return Vector(round(self.x / self.get_length(), 2),
                      round(self.y / self.get_length(), 2))

    def angle_between(self, other: Vector) -> int:
        abs_angle = abs(
            + round(
                math.degrees(
                    math.atan2(self.y / self.get_length(),
                               self.x / self.get_length())
                )
            )
            - round(
                math.degrees(
                    math.atan2(other.y / self.get_length(),
                               other.x / self.get_length())
                )
            )
        )
        if abs_angle > 180:
            return 360 - abs_angle
        return abs_angle

    def get_angle(self) -> int:
        return round(
            math.degrees(
                math.acos(self.y / self.get_length())
            )
        )

    def rotate(self, degrees: int) -> Vector:
        initial_angle = math.atan2(
            self.y / self.get_length(),
            self.x / self.get_length()
        )
        final_angle = initial_angle + math.radians(degrees)
        return Vector(
            round(math.cos(final_angle) * self.get_length(), 2),
            round(math.sin(final_angle) * self.get_length(), 2))
