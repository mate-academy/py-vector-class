from __future__ import annotations
import math


class Vector:
    def __init__(self, cor_x: int | float, cor_y: int | float) -> None:
        self.x = round(cor_x, 2)
        self.y = round(cor_y, 2)

    def __add__(self, not_self: Vector) -> Vector:
        return Vector(self.x + not_self.x, self.y + not_self.y)

    def __sub__(self, not_self: Vector) -> Vector:
        return Vector(self.x - not_self.x, self.y - not_self.y)

    def __mul__(self, not_self: Vector | int | float) -> Vector | int | float:
        if isinstance(not_self, Vector):
            return ((self.x * not_self.x)
                    + (self.y * not_self.y))
        return Vector(self.x * not_self, self.y * not_self)

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple) -> Vector:
        return Vector((end[0] - start[0]), (end[1] - start[1]))

    def get_length(self) -> int | float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(),
                      self.y / self.get_length()
                      )

    def angle_between(self, vec2: Vector) -> int:
        return round(
            math.degrees(
                math.acos(
                    self.__mul__(vec2)
                    / (self.get_length()
                       * vec2.get_length())
                )
            )
        )

    def get_angle(self) -> int:
        pos_y = Vector(0, 1)
        return round(
            math.degrees(
                math.acos(
                    self.__mul__(pos_y)
                    / (self.get_length() * pos_y.get_length())
                )
            )
        )

    def rotate(self, degree: int) -> Vector:
        rad = math.radians(degree)
        cor_x = (self.x * math.cos(rad)) - (self.y * math.sin(rad))
        cor_y = (self.x * math.sin(rad)) + (self.y * math.cos(rad))
        return Vector(cor_x, cor_y)
