from __future__ import annotations
import math


class Vector:
    def __init__(self, p_x: float, p_y: float) -> None:
        self.x = round(p_x, 2)
        self.y = round(p_y, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            new_vector = Vector(
                p_x=self.x + other.x,
                p_y=self.y + other.y
            )
        else:
            raise ValueError(f"{other} should be Vector type")
        return new_vector

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            new_vector = Vector(
                p_x=self.x - other.x,
                p_y=self.y - other.y
            )
        else:
            raise ValueError(f"{other} should be Vector type")
        return new_vector

    def __mul__(self, other: Vector | int | float) -> Vector | float:
        if isinstance(other, (int, float)):
            new_vector = Vector(
                p_x=self.x * other,
                p_y=self.y * other
            )
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            raise ValueError(f"{other} should be Vector or int or float type")
        return new_vector

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        p_x = end_point[0] - start_point[0]
        p_y = end_point[1] - start_point[1]
        return cls(p_x, p_y)

    def get_normalized(self) -> Vector:
        new_vect = Vector(
            p_x=round(self.x / self.get_length(), 2),
            p_y=round(self.y / self.get_length(), 2)
        )
        return new_vect

    def angle_between(self, other: Vector) -> int:
        if isinstance(other, Vector):
            dot_prod = self.x * other.x + self.y * other.y
            cos_a = dot_prod / (self.get_length() * other.get_length())
            res = round(math.degrees(math.acos(cos_a)))
        else:
            raise ValueError(f"{other} should be Vector type")
        return res

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        new_vect = Vector(
            p_x=self.x * math.cos(radians) - self.y * math.sin(radians),
            p_y=self.x * math.sin(radians) + self.y * math.cos(radians)
        )
        return new_vect
