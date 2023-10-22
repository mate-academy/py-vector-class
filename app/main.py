from __future__ import annotations
import math


class Vector:
    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0], end_point[1] - start_point[1]
        )

    def __init__(
            self,
            x_coor: float | int,
            y_coor: float | int
    ) -> None:
        self.x = round(x_coor, 2)
        self.y = round(y_coor, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, other: int | float | Vector) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> float:
        return round(
            math.degrees(
                math.acos(
                    self.__mul__(other)
                    / self.get_length()
                    / other.get_length()
                )
            )
        )

    def get_angle(self) -> float:
        return self.angle_between(Vector(0, 5))

    def rotate(self, degrees: int) -> Vector:
        # x2 = cosβx1−sinβy1
        # y2 = sinβx1 + cosβy1
        x2 = (math.cos(math.radians(degrees)) * self.x
              - math.sin(math.radians(degrees)) * self.y)
        y2 = (math.cos(math.radians(degrees)) * self.y
              + math.sin(math.radians(degrees)) * self.x)
        return Vector(x2, y2)
