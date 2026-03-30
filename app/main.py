from __future__ import annotations
import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(
            x=self.x + other.x,
            y=self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(
            x=self.x - other.x,
            y=self.y - other.y)

    def __mul__(self, other: float | "Vector") -> float | "Vector":
        if isinstance(other, Vector):
            return (self.y * other.y) + (self.x * other.x)

        return Vector(x=self.x * other, y=self.y * other)

    @staticmethod
    def create_vector_by_two_points(
            start_point: tuple,
            end_point: tuple
    ) -> "Vector":
        point1 = Vector(start_point[0], start_point[1])
        point2 = Vector(end_point[0], end_point[1])
        return point2.__sub__(point1)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> "Vector":
        return Vector(
            x=self.x / Vector.get_length(self),
            y=self.y / Vector.get_length(self)
        )

    def angle_between(self, other: "Vector") -> int:
        mul = self.__mul__(other)
        a = Vector.get_length(self)
        b = Vector.get_length(other)
        cos_a = mul / (a * b)
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        other = Vector(0, 1)
        return Vector.angle_between(self, other)

    def rotate(self, degrees: int) -> "Vector":
        radian = math.radians(degrees)
        new_x = self.x * math.cos(radian) - self.y * math.sin(radian)
        new_y = self.x * math.sin(radian) + self.y * math.cos(radian)
        return Vector(new_x, new_y)
