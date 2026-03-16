from __future__ import annotations
import math


class Vector:

    def __init__(self, x_coord: int | float, y_coord: int | float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            x_coord=self.x + other.x,
            y_coord=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            x_coord=self.x - other.x,
            y_coord=self.y - other.y
        )

    def __mul__(self, other: int | float | Vector) -> Vector | int | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(
            x_coord=self.x * other,
            y_coord=self.y * other
        )

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple) -> Vector:
        return cls(
            x_coord=(end[0] - start[0]),
            y_coord=(end[1] - start[1])
        )

    def get_length(self) -> int | float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(
            x_coord=self.x / length,
            y_coord=self.y / length
        )

    def angle_between(self, other: Vector) -> int:
        mul_scal = self.__mul__(other)
        a_length = self.get_length()
        b_length = other.get_length()
        cos_a = mul_scal / (a_length * b_length)
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int | float:
        deg = math.degrees(math.atan2(self.x, self.y))
        deg = ((deg + 360) % 360)
        if deg > 180:
            deg = 360 - deg
        return round(deg)

    def rotate(self, degree: int) -> Vector:
        new_x = (self.x * math.cos(math.radians(degree))
                 - self.y * math.sin(math.radians(degree)))
        new_y = (self.x * math.sin(math.radians(degree))
                 + self.y * math.cos(math.radians(degree)))
        return Vector(x_coord=new_x, y_coord=new_y)
