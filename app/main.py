from __future__ import annotations
import math


class Vector:

    def __init__(self, xx: float, yy: float) -> None:
        self.x = round(xx, 2)
        self.y = round(yy, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x,
                      self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x,
                      self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> Vector | float | int:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other,
                      self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[-1] - start_point[-1])

    def get_length(self) -> int | float:
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / abs(self.get_length()),
                      self.y / abs(self.get_length()))

    def angle_between(self, other: Vector) -> int:
        cos_a = (self * other / (abs((self.x ** 2 + self.y ** 2) ** 0.5)
                                 * abs((other.x ** 2 + other.y ** 2) ** 0.5)))
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        if self.x < 0 and self.y < 0:
            return 180 - round(math.degrees(math.atan(abs(self.x / self.y))))
        else:
            return round(math.degrees(math.atan(abs(self.x / self.y))))

    def rotate(self, degrees: int) -> Vector:
        ang = math.radians(degrees)
        xr = (self.x * math.cos(ang)) - (self.y * math.sin(ang))
        yr = (self.x * math.sin(ang)) + (self.y * math.cos(ang))
        return Vector(round(xr, 2), round(yr, 2))
