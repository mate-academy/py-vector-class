from __future__ import annotations
import math


class Vector:
    def __init__(self, koord_x: float, koord_y: float) -> None:
        self.x = round(koord_x, 2)
        self.y = round(koord_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(koord_x=self.x + other.x, koord_y=self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(koord_x=self.x - other.x, koord_y=self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(koord_x=self.x * other, koord_y=self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple
                                    ) -> Vector:
        koord_x = end_point[0] - start_point[0]
        koord_y = end_point[1] - start_point[1]
        return cls(koord_x, koord_y)

    def get_length(self) -> float:
        return pow(self.x ** 2 + self.y ** 2, 0.5)

    def get_normalized(self) -> Vector:
        koord_x = self.x / self.get_length()
        koord_y = self.y / self.get_length()
        return Vector(koord_x, koord_y)

    def angle_between(self, other: Vector) -> int:
        angle = math.degrees(
            math.acos(
                (self * other)
                / (self.get_length() * other.get_length())
            )
        )
        return round(angle)

    def get_angle(self) -> int:
        y_axis = Vector(0, 1)
        angle = math.degrees(
            math.acos(
                (self * y_axis)
                / (self.get_length() * y_axis.get_length())
            )
        )
        return int(angle)

    def rotate(self, degrees: int) -> Vector:
        koord_x = (math.cos(math.radians(degrees)) * self.x
                   - math.sin(math.radians(degrees)) * self.y)
        koord_y = (math.sin(math.radians(degrees)) * self.x
                   + math.cos(math.radians(degrees)) * self.y)
        return Vector(koord_x, koord_y)
