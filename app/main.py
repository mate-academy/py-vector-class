from __future__ import annotations
import math


class Vector:
    def __init__(self, xx: float, yy: float) -> None:
        self.x = round(xx, 2)
        self.y = round(yy, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            xx=self.x + other.x,
            yy=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            xx=self.x - other.x,
            yy=self.y - other.y
        )

    def __mul__(self, other: Vector | float | int) -> Vector | int | float:
        if isinstance(other, (int, float)):
            return Vector(
                xx=self.x * other,
                yy=self.y * other
            )
        else:
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(
            xx=end_point[0] - start_point[0],
            yy=end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** (1 / 2)

    def get_normalized(self) -> Vector:
        return Vector(
            xx=self.x / self.get_length(),
            yy=self.y / self.get_length()
        )

    def angle_between(self, other: Vector) -> int:
        return round(math.degrees(math.acos(
            ((self.x * other.x) + (self.y * other.y))
            / (self.get_length() * other.get_length()))))

    def get_angle(self) -> int:
        return round(math.degrees(math.acos(
            self.y
            / (self.x ** 2 + self.y ** 2) ** (1 / 2))))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        return Vector(
            xx=self.x * math.cos(radians) - self.y * math.sin(radians),
            yy=self.x * math.sin(radians) + self.y * math.cos(radians)
        )
