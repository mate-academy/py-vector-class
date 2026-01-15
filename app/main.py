from __future__ import annotations
import math


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.x + other.x,
            self.y + other.y,
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x - other.x,
            self.y - other.y,
        )

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, (int, float, )):
            return Vector(
                self.x * other,
                self.y * other,
            )

        elif isinstance(other, Vector):
            return (self.x * other.x + self.y * other.y)

        raise TypeError("Unsupported type for arithmetic with Distance")

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple) -> Vector:
        return cls(
            end[0] - start[0],
            end[1] - start[1],
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        if self.get_length() == 0:
            return Vector(0, 0)
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> float:
        return round(math.degrees(
            math.acos(self.__mul__(other)
                      / (self.get_length() * other.get_length())
                      )))

    def rotate(self, degrees: int) -> Vector:
        rad = math.radians(degrees)
        x_rot = self.x * math.cos(rad) - self.y * math.sin(rad)
        y_rot = self.x * math.sin(rad) + self.y * math.cos(rad)
        return Vector(x_rot, y_rot)

    def get_angle(self) -> float:
        if not self.get_length():
            return 0
        cos_angle = self.y / self.get_length()
        cos_angle = max(-1, min(1, cos_angle))
        angle_degrees = math.degrees(math.acos(cos_angle))
        return round(angle_degrees)
