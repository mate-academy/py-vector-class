from __future__ import annotations

import math


class Vector:
    def __init__(self, vec_x: float, vec_y: float) -> None:
        self.x = round(vec_x, 2)
        self.y = round(vec_y, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Unsupported operand type for +: "
                            "'Vector' and '{}'".format(type(other)))

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        else:
            raise TypeError("Unsupported operand type for -: "
                            "'Vector' and '{}'".format(type(other)))

    def __mul__(self, other: Vector) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        else:
            raise TypeError("Unsupported operand type for *: "
                            "'Vector' and '{}'".format(type(other)))

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        vec_x = end_point[0] - start_point[0]
        vec_y = end_point[1] - start_point[1]
        return cls(vec_x, vec_y)

    def get_length(self) -> int | float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length != 0:
            return Vector(self.x / length, self.y / length)
        else:
            return Vector(0, 0)

    def angle_between(self, vector: Vector) -> int | float:
        dot_product = self * vector
        length_product = self.get_length() * vector.get_length()
        if length_product != 0:
            cos_theta = dot_product / length_product
            theta = math.degrees(math.acos(cos_theta))
            return round(theta)
        else:
            return 0

    def get_angle(self) -> int | float:
        reference_vector = Vector(0, 1)
        return self.angle_between(reference_vector)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
        rot_x = self.x * cos_theta - self.y * sin_theta
        rot_y = self.x * sin_theta + self.y * cos_theta
        return Vector(rot_x, rot_y)
