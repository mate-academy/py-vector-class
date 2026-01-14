from __future__ import division, annotations
from typing import Union
import math


class Vector:

    def __init__(self, x_: float, y_: float) -> None:
        self.x = round(x_, 2)
        self.y = round(y_, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(x_=self.x + other.x,
                      y_=self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(x_=self.x - other.x,
                      y_=self.y - other.y)

    def __mul__(self,
                other: Union[int, float, Vector]
                ) -> Union[float, Vector]:
        if isinstance(other, Vector):
            return ((self.x * other.x) + (self.y * other.y))
        else:
            return Vector(x_=round((self.x * other), 2),
                          y_=round((self.y * other), 2)
                          )

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple
                                    ) -> Vector:
        return cls(x_=round((end_point[0] - start_point[0]), 2),
                   y_=round((end_point[1] - start_point[1]), 2)
                   )

    def get_length(self) -> float:
        return ((self.x ** 2 + self.y ** 2) ** 0.5)

    def get_normalized(self) -> Vector:
        return Vector(x_=round((self.x / self.get_length()), 2),
                      y_=round((self.y / self.get_length()), 2)
                      )

    def angle_between(self, vector: Vector) -> int:
        cos_a = (self.__mul__(vector)
                 / (self.get_length() * vector.get_length()))
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        cos_a = (self.y / self.get_length())
        return int(math.degrees(math.acos(cos_a)))

    def rotate(self, angle: int) -> Vector:
        return Vector(
            x_=round((self.x * (math.cos(math.radians(angle)))
                     - self.y * (math.sin(math.radians(angle)))), 2),
            y_=round((self.y * (math.cos(math.radians(angle)))
                     + self.x * (math.sin(math.radians(angle)))), 2)
        )
