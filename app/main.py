from __future__ import annotations
import math


class Vector:
    def __init__(self, x_num: float, y_num: float) -> None:
        self.x = round(x_num, 2)  # - не работает
        self.y = round(y_num, 2)

    def __add__(self, other: int) -> Vector:
        res_x = self.x + other.x
        res_y = self.y + other.y
        res = Vector(res_x, res_y)
        return res

    def __sub__(self, other: int) -> Vector:
        res_x = self.x - other.x
        res_y = self.y - other.y
        res = Vector(res_x, res_y)
        return res

    def __mul__(self, other: int) -> Vector:
        if isinstance(other, Vector):
            res = self.x * other.x + self.y * other.y
            return res
        else:
            res_x = round(self.x * other, 2)
            res_y = round(self.y * other, 2)
            res = Vector(res_x, res_y)
            return res

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        start = cls(x_num=start_point[0], y_num=start_point[1])
        end = cls(x_num=end_point[0], y_num=end_point[1])
        return end - start

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        self.x = round(self.x / length, 2)
        self.y = round(self.y / length, 2)
        return self

    def angle_between(self, other: int) -> int:
        vector_modul1 = self.get_length()
        vector_modul2 = other.get_length()
        scale_dob = self.x * other.x + self.y * other.y
        cos_angle = scale_dob / (vector_modul1 * vector_modul2)
        angle = math.degrees(math.acos(cos_angle))
        return round(angle)

    def get_angle(self) -> int:
        vect = Vector(0, 1)
        angle = (self * vect) / (self.get_length() * vect.get_length())
        return round(math.degrees(math.acos(angle)))

    def rotate(self, dgreeses: int) -> Vector:
        radian = math.radians(dgreeses)
        return Vector(
            math.cos(radian) * self.x - math.sin(radian) * self.y,
            math.sin(radian) * self.x + math.cos(radian) * self.y
        )
