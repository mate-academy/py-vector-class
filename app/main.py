import math
from typing import Union


class Vector:
    def __init__(self, point_x: float, point_y: float) -> None:
        if isinstance(point_x, tuple) and isinstance(point_y, tuple):
            self.x = round(point_x[0], 2)
            self.y = round(point_y[-1], 2)
        else:
            self.x = round(point_x, 2)
            self.y = round(point_y, 2)

    def __add__(self, other: Union["Vector", int, float]) -> "Vector":
        if isinstance(other, Vector):
            return Vector((self.x + other.x), (self.y + other.y))

    def __sub__(self, other: Union["Vector", int, float]) -> "Vector":
        if isinstance(other, Vector):
            return Vector((self.x - other.x), (self.y - other.y))

    def __mul__(self, other: Union["Vector", int, float]) -> ("Vector", float):
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector(self.x * other, (self.y * other))

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> "Vector":
        start_point_x, start_point_y = start_point
        end_point_x, end_point_y = end_point
        return cls(
            (end_point_x - start_point_x),
            (end_point_y - start_point_y)
        )

    def get_length(self) -> float:
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def get_normalized(self) -> "Vector":
        return Vector(round(self.x / self.get_length(), 2),
                      round(self.y / self.get_length(), 2))

    def angle_between(self, other: Union["Vector", int, float]) -> int:
        cos_a = (self * other) / (abs(self.get_length())
                                  * abs(other.get_length()))
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self) -> int:
        cos_a1 = self.y / self.get_length()
        return round(math.degrees(math.acos(cos_a1)))

    def rotate(self, other: ("Vector", float, int)) -> "Vector":
        radians = math.radians(other)
        cos_angle = math.cos(radians)
        sin_angle = math.sin(radians)
        rot_x = self.x * cos_angle - self.y * sin_angle
        rot_y = self.x * sin_angle + self.y * cos_angle
        return Vector(rot_x, rot_y)
