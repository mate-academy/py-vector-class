from __future__ import annotations
import math


class Vector:
    def __init__(self, x_cord: float, y_cord: float) -> None:
        self.x = round(x_cord, 2)
        self.y = round(y_cord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector((self.x + other.x), (self.y + other.y))

    def __sub__(self, other: Vector) -> Vector:
        return Vector((self.x - other.x), (self.y - other.y))

    def __mul__(self, other: int | float | Vector) -> any:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return float((self.x * other.x) + (self.y * other.y))

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return (self.x**2 + self.y**2)**.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        x_cord = self.x / length
        y_cord = self.y / length
        return Vector(x_cord, y_cord)

    def angle_between(self, other: Vector) -> int:
        self_len = self.get_length()
        other_len = Vector.get_length(other)

        if self_len and other_len:
            tmp = self.__mul__(other) / (self_len * other_len)
            return int(round(math.degrees(math.acos(tmp))))

    def get_angle(self) -> int:
        return abs(round(math.degrees(math.atan2(self.x, self.y))))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        x_cord = round((self.x * math.cos(radians)
                        - self.y * math.sin(radians)), 2)
        y_cord = round((self.x * math.sin(radians)
                        + self.y * math.cos(radians)), 2)
        return Vector(x_cord, y_cord)
