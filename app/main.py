from __future__ import annotations

import math


class Vector:
    def __init__(self, x_coord: int | float, y_coord: int | float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple[int | float],
            end_point: tuple[int | float]) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> int | float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        module = (self.x ** 2 + self.y ** 2) ** 0.5
        return Vector(self.x / module, self.y / module)

    def angle_between(self, other: Vector) -> int:
        return round(math.degrees(math.acos(
            ((self * other)
             / ((self.x ** 2 + self.y ** 2) ** 0.5
             * (other.x ** 2 + other.y ** 2) ** 0.5)))))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        self.x, self.y = (round(math.cos(radians) * self.x
                                - math.sin(radians) * self.y, 2),
                          round(math.sin(radians) * self.x
                                + math.cos(radians) * self.y, 2))
        return self
