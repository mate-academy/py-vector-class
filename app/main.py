from __future__ import annotations
import math


class Vector:

    def __init__(self, self_x : int, self_y : int) -> None:
        self.x = round(self_x, 2)
        self.y = round(self_y, 2)

    def __add__(self, other: Vector) -> Vector:
        vector3 = Vector(self.x + other.x, self.y + other.y)
        return vector3

    def __sub__(self, other: Vector) -> Vector:
        vector3 = Vector(self.x - other.x, self.y - other.y)
        return vector3

    def __mul__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return (self.x * other.x + self.y * other.y)
        vector3 = Vector(self.x * other, self.y * other)
        return vector3

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:

        return Vector(end_point[0] - start_point[0],
                      end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.hypot(self.x, self.y)

    def get_normalized(self) -> int:
        return Vector(self.x / math.hypot(self.x, self.y),
                      self.y / math.hypot(self.x, self.y))

    def angle_between(self, other: Vector) -> int:
        dobutok = (self.x * other.x + self.y * other.y)
        return round(math.degrees(
            math.acos(dobutok / (self.get_length() * other.get_length()))))

    def get_angle(self) -> float:
        return round(math.degrees(math.acos(self.y / self.get_length())))

    def rotate(self, degrees: int) -> Vector:
        radian = math.radians(degrees)
        new_vector_x = self.x * math.cos(radian) - self.y * math.sin(radian)
        new_vector_y = self.y * math.cos(radian) + self.x * math.sin(radian)
        return Vector(new_vector_x, new_vector_y)
