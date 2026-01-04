from __future__ import annotations

import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0], end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return math.hypot(self.x, self.y)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length < 1e-9:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        angule = (
            abs(
                round(
                    math.degrees(
                        math.atan2(
                            self.x * other.y - self.y * other.x,
                            self.x * other.x + self.y * other.y,
                        )
                    )
                )
            )
            % 360
        )
        return angule

    def get_angle(self) -> int:
        angle = abs(round(math.degrees(math.atan2(self.x, self.y))))
        return angle

    def rotate(self, degrees: float) -> Vector:
        radians = math.radians(degrees)
        return Vector(
            self.x * math.cos(radians) - self.y * math.sin(radians),
            self.x * math.sin(radians) + self.y * math.cos(radians),
        )
