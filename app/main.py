from __future__ import annotations
import math


class Vector:
    def __init__(self, xp: float, yp: float) -> None:
        self.x = round(xp, 2)
        self.y = round(yp, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            xp=self.x + other.x,
            yp=self.y + other.y,
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            xp=self.x - other.x,
            yp=self.y - other.y,
        )

    def __mul__(self, other: float | Vector) -> Vector | float:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector(
            xp=self.x * other,
            yp=self.y * other,
        )

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple
                                    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1],
        )

    def get_length(self) -> float:
        return math.sqrt(
            (self.x ** 2) + (self.y ** 2)
        )

    def get_normalized(self) -> Vector:
        return Vector(
            xp=self.x / math.sqrt((self.x ** 2) + (self.y ** 2)),
            yp=self.y / math.sqrt((self.x ** 2) + (self.y ** 2)),
        )

    def angle_between(self, other: Vector) -> int:
        return round(
            math.degrees(
                math.acos(
                    ((self.x * other.x) + (self.y * other.y))
                    / (math.sqrt((self.x ** 2) + (self.y ** 2))
                       * math.sqrt((other.x ** 2) + (other.y ** 2)))
                )))

    def get_angle(self) -> float:
        return round(
            math.degrees(
                math.acos(
                    ((self.x * 0) + (self.y * 10))
                    / (math.sqrt((self.x ** 2) + (self.y ** 2))
                       * math.sqrt((0 ** 2) + (10 ** 2)))
                )))

    def rotate(self, degrees: int) -> Vector:
        return Vector(
            xp=(self.x * math.cos(
                math.radians(degrees)
            )) - (self.y * math.sin(
                math.radians(degrees)
            )),
            yp=(self.x * math.sin(
                math.radians(degrees)
            )) + (self.y * math.cos(
                math.radians(degrees)
            )),
        )
