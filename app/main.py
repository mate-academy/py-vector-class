from __future__ import annotations
import math


class Vector:
    def __init__(self, x_cord: float, y_cord: float) -> None:
        self.x = round(x_cord, 2)
        self.y = round(y_cord, 2)

    def __add__(self, new: "Vector") -> "Vector":
        if isinstance(new, Vector):
            return Vector(self.x + new.x, self.y + new.y)

    def __sub__(self, new: "Vector") -> "Vector":
        if isinstance(new, Vector):
            return Vector(self.x - new.x, self.y - new.y)

    def __mul__(self, mult: Vector | float) -> Vector:
        if isinstance(mult, (int, float)):
            return Vector(self.x * mult, self.y * mult)
        else:
            return (self.x * mult.x) + (self.y * mult.y)

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple) -> Vector:
        return cls(end[0] - start[0], end[1] - start[1])

    def get_length(self) -> float:
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def get_angle(self) -> int:
        return abs(round(math.degrees(math.atan2(self.x, self.y))))

    def angle_between(self, new: Vector) -> int:
        self_length = self.get_length()
        other_length = Vector.get_length(new)

        if self_length and other_length:
            cosine = self.__mul__(new) / (self_length * other_length)
            return int(round(math.degrees(math.acos(cosine))))

    def rotate(self, deg: int) -> Vector:
        cosine = math.cos(math.radians(deg))
        sinus = math.sin(math.radians(deg))
        return Vector(
            self.x * cosine - self.y * sinus,
            self.x * sinus + self.y * cosine)
