from __future__ import annotations
import math


class Vector:

    def __init__(self, x_axis: float, y_axis: float) -> None:

        self.x = round(x_axis, 2)
        self.y = round(y_axis, 2)
        self.length = Vector.get_length(self)

    def __add__(self, other: Vector) -> Vector:

        new_x = self.x + other.x
        new_y = self.y + other.y

        return Vector(new_x, new_y)

    def __sub__(self, other: Vector) -> Vector:

        new_x = self.x - other.x
        new_y = self.y - other.y

        return Vector(new_x, new_y)

    def __mul__(self, other: (Vector, float, int))\
            -> (Vector, float, int):

        if isinstance(other, Vector):

            return (self.x * other.x) + (self.y * other.y)

        new_x = self.x * other
        new_y = self.y * other

        return Vector(new_x, new_y)

    @classmethod
    def create_vector_by_two_points(cls, 
                                    start_point: tuple, 
                                    end_point: tuple
                                   ) -> Vector:

        new_x = end_point[0] - start_point[0]
        new_y = end_point[1] - start_point[1]

        return Vector(new_x, new_y)

    def get_length(self) -> float:

        vector_len = (self.x ** 2 + self.y ** 2) ** (1 / 2)

        return vector_len

    def get_normalized(self) -> Vector:

        norm_x = round(self.x / self.length, 2)
        norm_y = round(self.y / self.length, 2)

        return Vector(norm_x, norm_y)

    def angle_between(self, other: Vector) -> (int, float):

        cos_a = (self * other) / (self.length * other.length)
        angle = math.degrees(math.acos(cos_a))

        return round(angle)

    def get_angle(self) -> (int, float):

        cos_a = self.y / self.length
        angle = math.degrees(math.acos(cos_a))

        return round(angle)

    def rotate(self, degrees: int) -> Vector:

        degrees = math.radians(degrees)
        rotated_x = self.x * math.cos(degrees) - self.y * math.sin(degrees)
        rotated_y = self.y * math.cos(degrees) + self.x * math.sin(degrees)

        return Vector(rotated_x, rotated_y)
