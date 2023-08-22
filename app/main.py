from __future__ import annotations
from math import sqrt, acos, cos, sin, radians, degrees


class Vector:
    def __init__(self, x_cor: float, y_cor: float) -> None:
        self.x = round(x_cor, 2)
        self.y = round(y_cor, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(x_cor=self.x + other.x, y_cor=self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(x_cor=self.x - other.x, y_cor=self.y - other.y)

    def __mul__(self, mul: int | float | Vector) -> Vector | float | int:
        if isinstance(mul, int | float):
            return Vector(x_cor=self.x * mul, y_cor=self.y * mul)
        else:
            return self.x * mul.x + self.y * mul.y

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple) -> Vector:
        return cls(x_cor=end[0] - start[0], y_cor=end[1] - start[1])

    def get_length(self) -> int | float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        ln = self.get_length()
        return Vector(x_cor=self.x / ln, y_cor=self.y / ln)

    def angle_between(self, other: Vector) -> float:
        return round(degrees(acos(self.__mul__(other)
                                  / (self.get_length() * other.get_length()))))

    def get_angle(self) -> float:
        s_len = self.get_length()
        v2 = Vector(0, 1)
        ref_len = v2.get_length()
        dot_p = self.__mul__(v2)
        ang = degrees(acos(dot_p / (s_len * ref_len)))
        return round(ang)

    def rotate(self, angl: int) -> Vector:
        y_cor = self.y
        s_len = self.get_length()
        v2 = Vector(1, 0)
        ref_len = v2.get_length()
        dot_p = self.__mul__(v2)
        ang_0 = (y_cor / abs(y_cor)) * degrees(acos(dot_p / (s_len * ref_len)))
        if angl + ang_0 < 360:
            ang_sum = radians(angl + ang_0)
        else:
            ang_sum = radians(angl + ang_0 - 360)
        return Vector(x_cor=s_len * cos(ang_sum),
                      y_cor=s_len * sin(ang_sum)
                      )
