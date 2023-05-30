from __future__ import annotations
import math


class Vector:
    def __init__(self, pos_x: int | float, pos_y: int | float) -> None:
        self.x = round(pos_x, 2)
        self.y = round(pos_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector((self.x + other.x), (self.y + other.y))

    def __sub__(self, other: Vector) -> Vector:
        return Vector((self.x - other.x), (self.y - other.y))

    def __mul__(self, multiplier: int | float | Vector) -> Vector:
        if not isinstance(multiplier, Vector):
            return Vector((self.x * multiplier), (self.y * multiplier))

        else:
            return (self.x * multiplier.x + self.y * multiplier.y)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return Vector((end_point[0] - start_point[0]),
                      (end_point[1] - start_point[1]))

    def get_length(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector | float) -> float:
        angle_radians = math.acos(
            (self * other) / (self.get_length() * other.get_length()))
        return round(math.degrees(angle_radians))

    def get_angle(self) -> float:
        return round(math.sqrt(math.degrees(math.atan2(self.x, self.y))**2))

    # x2 = r−u = cosβx1−sinβy1
    # y2 = t + s = sinβx1 + cosβy1

    def rotate(self, degrees: float | int) -> Vector:
        angle_rad = math.radians(degrees)
        new_x = math.cos(angle_rad) * self.x - math.sin(angle_rad) * self.y
        new_y = math.sin(angle_rad) * self.x + math.cos(angle_rad) * self.y

        return Vector(new_x, new_y)
