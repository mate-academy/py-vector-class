from __future__ import annotations
from typing import Union
import math


class Vector:
    def __init__(self, x_coord: int, y_coord: int) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

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

    def __mul__(self, other: Union[int, Vector]) -> Union[float, Vector]:
        if type(other) == int or type(other) == float:
            return Vector(
                self.x * other,
                self.y * other
            )
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) \
            -> Vector:
        if start_point[0] < 0 or start_point[1] < 0 or \
                end_point[0] < 0 or end_point[1] < 0:
            return cls(
                end_point[0] - start_point[0],
                end_point[1] - start_point[1]
            )
        return cls(
            end_point[0] + start_point[0],
            end_point[1] + start_point[1]
        )

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length()
        )

    def angle_between(self, vector: Vector) -> int:
        return round(math.degrees(
            math.acos((self.x * vector.x + self.y * vector.y)
                      / (self.get_length() * vector.get_length()))))

    def get_angle(self) -> int:
        vector = Vector(0, 9)
        return vector.angle_between(self)

    def rotate(self, degrees: int) -> Vector:
        return Vector(
            (self.x * math.cos(math.radians(degrees))
             - self.y * math.sin(math.radians(degrees))),
            (self.x * math.sin(math.radians(degrees))
             + self.y * math.cos(math.radians(degrees)))
        )
