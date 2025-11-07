from __future__ import annotations

from math import degrees, cos, sin, radians, acos


class Vector:

    def __init__(self, x: float, y: float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> float | Vector | None:
        if isinstance(other, int) or isinstance(other, float):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        cos_theta = self * other / (self.get_length() * other.get_length())
        in_radian = acos(cos_theta)
        in_degrees = degrees(in_radian)
        return round(in_degrees)

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        return Vector(
            self.x * cos(radians(degrees)) - self.y * sin(radians(degrees)),
            self.x * sin(radians(degrees)) + self.y * cos(radians(degrees)))


vector = Vector(-4.44, 5.2)
vector.angle_between(Vector(15, -76))
