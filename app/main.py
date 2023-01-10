
from typing import Any
import math


class Vector:
    def __init__(self, ox: float, oy: float) -> None:
        self.x = round(ox, 2)
        self.y = round(oy, 2)

    def __add__(self, other: Any) -> Any:
        if isinstance(other, Vector):
            return Vector(
                ox=self.x + other.x,
                oy=self.y + other.y)

    def __sub__(self, other: Any) -> Any:
        if isinstance(other, Vector):
            return Vector(
                ox=self.x - other.x,
                oy=self.y - other.y)

    def __mul__(self, other: Any) -> Any:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(ox=self.x * other, oy=self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: Any,
                                    end_point: Any
                                    ) -> Any:
        return Vector(
            ox=end_point[0] - start_point[0],
            oy=end_point[1] - start_point[1])

    def get_length(self) -> Any:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Any:
        return Vector(
            ox=round(self.x / self.get_length(), 2),
            oy=round(self.y / self.get_length(), 2))

    def angle_between(self, other: Any) -> Any:
        cos_a = (self.__mul__(other)) / \
                (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> Any:
        cos_a = self.y / (self.get_length() * math.sqrt(0**2 + 1**2))
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: Any) -> Any:
        return Vector(
            ox=math.cos(math.radians(degrees))
            * self.x - math.sin(math.radians(degrees)) * self.y,
            oy=math.sin(math.radians(degrees))
            * self.x + math.cos(math.radians(degrees)) * self.y)
