from __future__ import annotations
from typing import Type, TypeVar
import math

Self = TypeVar("Self", bound="Vector")


class Vector:

    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x: float = round(x_coord, 2)
        self.y: float = round(y_coord, 2)

    def __add__(self: Self, vector: Self) -> Self:
        return self.__class__(self.x + vector.x, self.y + vector.y)

    def __sub__(self: Self, vector: Self) -> Self:
        return self.__class__(self.x - vector.x, self.y - vector.y)

    def __mul__(self: Self, other: float | Self) -> float | Self:
        if isinstance(other, (float, int)):
            return self.__class__(self.x * other, self.y * other)
        elif isinstance(other, self.__class__):
            return self.x * other.x + self.y * other.y
        raise TypeError

    @classmethod
    def create_vector_by_two_points(cls: Type[Self], start_point: tuple[float,
                                                                        float],
                                    end_point: tuple[float, float]) -> Self:
        x_: float = end_point[0] - start_point[0]
        y_: float = end_point[1] - start_point[1]
        return cls(x_, y_)

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self: Self) -> Self:
        length: float = self.get_length()
        return self.__class__(self.x / length, self.y / length)

    def angle_between(self: Self, vector: Self) -> int:
        cos_a: float = (self * vector) / (self.get_length()
                                          * vector.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        return round(math.degrees(math.acos(self.y / self.get_length())))

    def rotate(self: Self, degrees: int) -> Self:
        rad: float = math.radians(degrees)
        x_: float = self.x * math.cos(rad) - self.y * math.sin(rad)
        y_: float = self.x * math.sin(rad) + self.y * math.cos(rad)
        return self.__class__(x_, y_)
