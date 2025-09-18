from __future__ import annotations
import math


class Vector:
    def __init__(self, end_x: float, end_y: float) -> None:
        self.x = round(end_x, 2)
        self.y = round(end_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return self.__class__(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return self.__class__(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return self.__class__(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return self.__class__(
            self.x / self.get_length(),
            self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> int:
        cos = (self * other) / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(cos)))

    def get_angle(self) -> int:
        return round(math.degrees(math.acos(self.y / self.get_length())))

    def rotate(self, degrees: int) -> Vector:
        degrees = math.radians(degrees)
        return self.__class__(
            self.x * math.cos(degrees) - self.y * math.sin(degrees),
            self.x * math.sin(degrees) + self.y * math.cos(degrees)
        )
