from __future__ import annotations
from typing import Union
import math


class Vector:
    def __init__(self, exs: int | float, ygr: int | float) -> None:
        self.x = round(exs, 2)
        self.y = round(ygr, 2)

    def __add__(self, vect: Vector) -> Vector:
        return Vector(
            exs=self.x + vect.x,
            ygr=self.y + vect.y
        )

    def __sub__(self, vect: Vector) -> Vector:
        return Vector(
            exs=self.x - vect.x,
            ygr=self.y - vect.y
        )

    def __mul__(self,
                other: Union[int, float, Vector]
                ) -> Union[Vector, float, int]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(
            exs=self.x * other,
            ygr=self.y * other
        )

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple
                                    ) -> Vector:
        return cls(
            exs=end_point[0] - start_point[0],
            ygr=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            exs=self.x / self.get_length(),
            ygr=self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> int:
        result = math.degrees(
            math.acos(
                self * other
                / (self.get_length() * other.get_length())
            )
        )
        return round(result)

    def get_angle(self) -> int:
        other = Vector(exs=0, ygr=10)
        return self.angle_between(other)

    def rotate(self, degrees: int) -> Vector:
        return Vector(
            exs=self.x * math.cos(math.radians(degrees))
            - self.y * math.sin(math.radians(degrees)),
            ygr=self.x * math.sin(math.radians(degrees))
            + self.y * math.cos(math.radians(degrees))
        )
