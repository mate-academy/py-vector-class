from __future__ import annotations
import math


# flake8: noqa

class Vector:
    def __init__(self, x: int | float, y: int | float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x,
                      self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x,
                      self.y - other.y)

    def __mul__(self, number: int | float | Vector) -> Vector | float | int:
        if isinstance(number, Vector):
            return self.x * number.x + \
                self.y * number.y

        return Vector(self.x * number, self.y * number)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1],
        )

    def get_length(self) -> int | float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / self.get_length(),
            self.y / self.get_length(),
        )

    def angle_between(self, other: Vector) -> int:
        prod = self.__mul__(other)
        u_mod = self.get_length()
        v_mod = other.get_length()
        cos_a = prod / (u_mod * v_mod)
        angle = math.degrees(math.acos(cos_a))
        return round(angle)

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        deg = math.radians(degrees)
        rotated_x = self.x * math.cos(deg) - self.y * math.sin(deg)
        rotated_y = self.x * math.sin(deg) + self.y * math.cos(deg)
        return Vector(rotated_x, rotated_y)
