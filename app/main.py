from __future__ import annotations

import math


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self._x = round(x_coordinate, 2)
        self._y = round(y_coordinate, 2)

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            round(self.x + other.x, 2),
            round(self.y + other.y, 2),
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            round(self.x - other.x, 2),
            round(self.y - other.y, 2),
        )

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        if isinstance(other, (int, float)):
            return Vector(
                round(self.x * other, 2),
                round(self.y * other, 2),
            )

        return NotImplemented

    @classmethod
    def create_vector_by_two_points(
        cls,
        start_point: tuple[float, float],
        end_point: tuple[float, float],
    ) -> Vector:
        return cls(
            round(end_point[0] - start_point[0], 2),
            round(end_point[1] - start_point[1], 2),
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()

        if length == 0:
            raise ValueError("Cannot normalize a zero-length vector")

        return Vector(
            round(self.x / length, 2),
            round(self.y / length, 2),
        )

    def angle_between(self, other: Vector) -> int:
        length_self = self.get_length()
        length_other = other.get_length()

        if length_self == 0 or length_other == 0:
            raise ValueError("Cannot compute angle with a zero-length vector")

        dot_product = self * other
        cos_theta = dot_product / (length_self * length_other)
        cos_theta = max(-1.0, min(1.0, cos_theta))

        return round(math.degrees(math.acos(cos_theta)))

    def get_angle(self) -> int:
        angle_radians = math.atan2(-self.x, self.y)
        angle_degrees = math.degrees(angle_radians)

        return round(angle_degrees % 360)

    def rotate(self, angle_degrees: int) -> Vector:
        angle_radians = math.radians(angle_degrees)

        cos_angle = math.cos(angle_radians)
        sin_angle = math.sin(angle_radians)

        new_x = self.x * cos_angle - self.y * sin_angle
        new_y = self.x * sin_angle + self.y * cos_angle

        return Vector(round(new_x, 2), round(new_y, 2))
