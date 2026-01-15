from __future__ import annotations
import math


class Vector:
    def __init__(self, point_x: int | float, point_y: int | float) -> None:
        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector((self.x + other.x),
                      (self.y + other.y))

    def __sub__(self, other: Vector) -> Vector:
        return Vector((self.x - other.x),
                      (self.y - other.y))

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, float | int):
            return Vector((self.x * other),
                          (self.y * other))
        return (self.x * other.x
                + self.y * other.y)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(),
                      self.y / self.get_length())

    def angle_between(self, other: Vector | float) -> float:
        angle_radians = math.acos((self * other)
                                  / (self.get_length() * other.get_length()))

        return round(math.degrees(angle_radians))

    def get_angle(self) -> float:
        return round(math.sqrt(math.degrees(
            math.atan2(self.x, self.y)) ** 2))

    def rotate(self, degrees: int | float) -> Vector:
        radian = math.radians(degrees)
        return Vector(
            math.cos(radian) * self.x - math.sin(radian) * self.y,
            math.sin(radian) * self.x + math.cos(radian) * self.y
        )
