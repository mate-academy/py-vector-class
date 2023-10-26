from __future__ import annotations
import math


class Vector:

    def __init__(self, coord_x: float, coord_y: float) -> None:
        self.x = round(coord_x, 2)
        self.y = round(coord_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    @staticmethod
    def dot_product(vec_1: Vector, vec_2: Vector) -> float:
        return vec_1.x * vec_2.x + vec_1.y * vec_2.y

    def __mul__(self, value: float | int | Vector) -> float | int | Vector:
        if isinstance(value, Vector):
            return self.dot_product(self, value)

        return Vector(self.x * value, self.y * value)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    @staticmethod
    def def_len(vec: Vector) -> float:
        return (vec.x ** 2 + vec.y ** 2) ** 0.5

    def get_length(self) -> float:
        return self.def_len(self)

    def get_normalized(self) -> Vector:
        len_ = self.def_len(self)
        return Vector(self.x / len_, self.y / len_)

    @classmethod
    def def_angle(cls, vec_1: Vector, vec_2: Vector) -> int:
        product = cls.dot_product(vec_1, vec_2)
        mod_1 = cls.def_len(vec_1)
        mod_2 = cls.def_len(vec_2)
        angle_float = math.degrees(math.acos(product / (mod_1 * mod_2)))
        return round(angle_float)

    def angle_between(self, other: Vector) -> int:
        return self.def_angle(self, other)

    def get_angle(self) -> int:
        other = Vector(0, int(math.fabs(self.y)))
        return self.def_angle(self, other)

    def rotate(self, angel: int) -> Vector:
        ang = math.radians(angel)
        return Vector(
            self.x * math.cos(ang) - self.y * math.sin(ang),
            self.x * math.sin(ang) + self.y * math.cos(ang)
        )
