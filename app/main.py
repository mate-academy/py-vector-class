from __future__ import annotations

import math


class Vector:
    def __init__(self, ordinate: float, abscissa: float) -> None:
        self.x = round(ordinate, 2)
        self.y = round(abscissa, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector | float:
        return self.__add__(Vector(-other.x, -other.y))

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, float) or isinstance(other, int):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[float | int],
            end_point: tuple[float | int]
    ) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def get_normalized(self) -> Vector:
        inv_length = 1 / self.get_length()
        return Vector(self.x * inv_length, self.y * inv_length)

    def angle_between(self, other: Vector) -> int:
        angle = math.acos(
            self * other
            / (self.get_length() * other.get_length())
        )
        return round(math.degrees(angle))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, angle: int) -> Vector:
        angle = angle * math.pi / 180
        rotate_dx = self.x * math.cos(angle) - self.y * math.sin(angle)
        rotate_dy = self.x * math.sin(angle) + self.y * math.cos(angle)
        return Vector(rotate_dx, rotate_dy)
