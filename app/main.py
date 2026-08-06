from __future__ import annotations
from math import sqrt, acos, degrees, radians, cos, sin


class Vector:
    def __init__(self, point_x: float, point_y: float) -> None:
        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x,
                      self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x,
                      self.y - other.y)

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other,
                      self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        lenght = self.get_length()
        return Vector(self.x / lenght,
                      self.y / lenght)

    def angle_between(self, vect: Vector) -> int:
        return round(degrees(acos(self.__mul__(vect)
                                  / (self.get_length() * vect.get_length()))))

    def get_angle(self) -> int:
        vector = Vector(0, 1)
        return self.angle_between(vector)

    def rotate(self, deg: int) -> Vector:
        point_x = self.x * cos(radians(deg)) - self.y * sin(radians(deg))
        point_y = self.y * cos(radians(deg)) + self.x * sin(radians(deg))
        return Vector(point_x, point_y)
