from __future__ import annotations
import math
from ctypes import Union


class Vector:
    def __init__(self, x_point: int, y_point: int) -> None:
        self.x = round(x_point, 2)
        self.y = round(y_point, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union[float, Vector]) -> Union[float, Vector]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> complex:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, vector: Vector) -> int:
        cos_a = self.__mul__(vector) \
            / (self.get_length() * vector.get_length())
        return round(math.degrees(math.acos(cos_a)), 0)

    def get_angle(self) -> int:
        angle_rad = math.atan2(self.y, self.x)
        angle_deg = math.degrees(angle_rad)
        return round((angle_deg - 90 + 360) % 360)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        x_new = self.x * math.cos(radians) - self.y * math.sin(radians)
        y_new = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(x_new, y_new)
