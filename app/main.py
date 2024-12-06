from __future__ import annotations

import math


class Vector:
    def __init__(
            self,
            cordinate_x: int | float,
            cordinate_y: int | float) -> None:
        self.x = round(cordinate_x, 2)
        self.y = round(cordinate_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            round(self.x + other.x, 2),
            round(self.y + other.y, 2)
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            round(self.x - other.x, 2),
            round(self.y - other.y, 2)
        )

    def __mul__(self, other: Vector | float | int) -> Vector | float:
        if isinstance(other, int | float):
            return Vector(
                round(self.x * other, 2),
                round(self.y * other, 2)
            )
        elif isinstance(other, Vector):
            return round(
                self.x * other.x
                + self.y * other.y,
                14
            )

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[int | float, int | float],
            end_point: tuple[int | float, int | float]
    ) -> Vector:
        return cls(
            round(end_point[0] - start_point[0], 2),
            round(end_point[1] - start_point[1], 2)
        )

    def get_length(self) -> float | int:
        return round(math.sqrt(self.x ** 2 + self.y ** 2), 15)

    def get_normalized(self) -> Vector:
        length = self.get_length()

        if length == 0:
            return Vector(0, 0)
        return Vector(
            round(self.x / length, 2),
            round(self.y / length, 2)
        )

    def angle_between(self, other: Vector) -> float:
        cos_vector = self * other / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_vector)))

    def get_angle(self) -> int:
        return int(math.degrees(math.acos(self.y / self.get_length())))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        x_new = (self.x * math.cos(radians)
                 - self.y * math.sin(radians))
        y_new = (self.x * math.sin(radians)
                 + self.y * math.cos(radians))
        return Vector(round(x_new, 2), round(y_new, 2))
