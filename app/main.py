
from typing import Any
import math


class Vector:
    def __init__(self, x_: float, y_: float) -> None:
        self.x = round(x_, 2)
        self.y = round(y_, 2)

    def __add__(self, other: Any) -> Any:
        if isinstance(other, Vector):
            return Vector(
                x_=self.x + other.x,
                y_=self.y + other.y)

    def __sub__(self, other: Any) -> Any:
        if isinstance(other, Vector):
            return Vector(
                x_=self.x - other.x,
                y_=self.y - other.y)

    def __mul__(self, other: Any) -> Any:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(x_=self.x * other, y_=self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: Any,
                                    end_point: Any
                                    ) -> Any:
        return Vector(
            x_=end_point[0] - start_point[0],
            y_=end_point[1] - start_point[1])

    def get_length(self) -> Any:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Any:
        return Vector(
            x_=round(self.x / self.get_length(), 2),
            y_=round(self.y / self.get_length(), 2))

    def angle_between(self, other: Any) -> Any:
        cos_a = (self.__mul__(other)) / \
                (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> Any:
        cos_a = self.y / (self.get_length() * math.sqrt(0**2 + 1**2))
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: Any) -> Any:
        return Vector(
            x_=math.cos(math.radians(degrees))
            * self.x - math.sin(math.radians(degrees)) * self.y,
            y_=math.sin(math.radians(degrees))
            * self.x + math.cos(math.radians(degrees)) * self.y)
