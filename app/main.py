from __future__ import annotations
import math


class Vector:

    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:

        self._X = round(x_coordinate, 2)
        self._Y = round(y_coordinate, 2)
        self.length = Vector.get_length(self)

    def __add__(self, other: Vector) -> Vector:

        new_x = self._X + other._X
        new_y = self._Y + other._Y

        return Vector(new_x, new_y)

    def __sub__(self, other: Vector) -> Vector:

        new_x = self._X - other._X
        new_y = self._Y - other._Y

        return Vector(new_x, new_y)

    def __mul__(self, other: (Vector, float, int))\
            -> (Vector, float, int):

        if isinstance(other, Vector):

            return (self._X * other._X) + (self._Y * other._Y)

        new_x = self._X * other
        new_y = self._Y * other

        return Vector(new_x, new_y)

    @classmethod
    def create_vector_by_two_points(
                                    cls,
                                    start_point: tuple,
                                    end_point: tuple
    ) -> Vector:

        new_x = end_point[0] - start_point[0]
        new_y = end_point[1] - start_point[1]

        return Vector(new_x, new_y)

    def get_length(self) -> float:

        vector_len = (self._X ** 2 + self._Y ** 2) ** (1 / 2)

        return vector_len

    def get_normalized(self) -> Vector:

        norm_x = round(self._X / self.length, 2)
        norm_y = round(self._Y / self.length, 2)

        return Vector(norm_x, norm_y)

    def angle_between(self, other: Vector) -> (int, float):

        cos_a = (self * other) / (self.length * other.length)
        angle = math.degrees(math.acos(cos_a))

        return round(angle)

    def get_angle(self) -> (int, float):

        cos_a = self._Y / self.length
        angle = math.degrees(math.acos(cos_a))

        return round(angle)

    def rotate(self, degrees: int):

        degrees = math.radians(degrees)
        rotated_x = self._X * math.cos(degrees) - self._Y * math.sin(degrees)
        rotated_y = self._Y * math.cos(degrees) + self._X * math.sin(degrees)

        return Vector(rotated_x, rotated_y)
