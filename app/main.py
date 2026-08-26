from __future__ import annotations
import math


class Vector:
    def __init__(self, x: int | float, y: int | float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x=self.x + other.x,
            y=self.y + other.y,
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x=self.x - other.x,
            y=self.y - other.y,
        )

    def __mul__(self, other: float | Vector) -> Vector | float:
        if not isinstance(other, Vector):
            return Vector(
                x=self.x * other,
                y=self.y * other,
            )
        else:
            return (self.x * other.x) + (self.y * other.y)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])

    def get_length(self) -> float:
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            x=self.x / self.get_length(),
            y=self.y / self.get_length(),
        )

    def angle_between(self, other: Vector) -> float:
        angle = self.__mul__(other) / \
            (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(angle)))

    def get_angle(self) -> float:
        angle = self.y / (self.get_length() * (1 ** 0.5))
        return round(math.degrees(math.acos(angle)))

    def rotate(self, ang: int) -> Vector:
        angle_rotate = math.radians(ang)
        return Vector(
            x=(math.cos(angle_rotate) * self.x)
            - (math.sin(angle_rotate) * self.y),
            y=(math.sin(angle_rotate) * self.x)
            + (math.cos(angle_rotate) * self.y),
        )
