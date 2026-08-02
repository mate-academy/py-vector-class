from __future__ import annotations
import math


class Vector:
    def __init__(self, pos_x: float | int, pos_y: float | int) -> None:
        self.x = round(pos_x, 2)
        self.y = round(pos_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            pos_x=self.x + other.x,
            pos_y=self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            pos_x=self.x - other.x,
            pos_y=self.y - other.y
        )

    def __mul__(self, other: Vector) -> Vector | int | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple
                                    ) -> Vector:
        return cls(
            pos_x=end_point[0] - start_point[0],
            pos_y=end_point[1] - start_point[1]
        )

    def get_length(self) -> int | float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        return Vector(
            pos_x=self.x / self.get_length(),
            pos_y=self.y / self.get_length()
        )

    def angle_between(self, other_v: Vector) -> int | float:
        dot = self.x * other_v.x + self.y * other_v.y
        len_a = self.get_length()
        len_b = other_v.get_length()
        cos = dot / (len_a * len_b)
        angle = math.degrees(math.acos(cos))

        return round(angle)

    def get_angle(self) -> int | float:
        length = self.get_length()

        cos = self.y / length

        angle = math.degrees(math.acos(cos))
        return round(angle)

    def rotate(self, deg: int) -> Vector:
        cos = math.cos(math.radians(deg))
        sin = math.sin(math.radians(deg))

        new_x = self.x * cos - self.y * sin
        new_y = self.x * sin + self.y * cos

        return Vector(pos_x=new_x, pos_y=new_y)
