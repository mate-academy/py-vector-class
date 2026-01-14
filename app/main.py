from __future__ import annotations
import math


class Vector:

    def __init__(self, point_x: float, point_y: float) -> None:
        self.x = round(point_x, 2)
        self.y = round(point_y, 2)

    def __add__(self, other: Vector | tuple) -> Vector:
        return Vector(self.x + other.x,
                      self.y + other.y)

    def __sub__(self, other: Vector | tuple) -> Vector:
        return Vector(self.x - other.x,
                      self.y - other.y)

    def __mul__(self, other: Vector | int) -> Vector | float:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        else:
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(
            self.x / Vector.get_length(self),
            self.y / Vector.get_length(self)
        )

    def angle_between(self, other: Vector) -> int:
        num = ((self.x * other.x) + (self.y * other.y)) / \
              (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(num)))

    def get_angle(self) -> int:
        return round(math.degrees(math.acos(self.y / self.get_length())))

    def rotate(self, degrees: int) -> Vector:
        cos_angle = math.cos(math.radians(degrees))
        sin_angle = math.sin(math.radians(degrees))
        return Vector((self.x * cos_angle - sin_angle * self.y),
                      (self.x * sin_angle + cos_angle * self.y))
