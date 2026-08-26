from __future__ import annotations
import math


class Vector:
    def __init__(
            self,
            x_coordinate: int | float,
            y_coordinate: int | float
    ) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        new_x = round(self.x + other.x, 2)
        new_y = round(self.y + other.y, 2)
        return Vector(new_x, new_y)

    def __sub__(self, other: Vector) -> Vector:
        new_x = round(self.x - other.x, 2)
        new_y = round(self.y - other.y, 2)
        return Vector(new_x, new_y)

    def __mul__(
            self,
            other: int | float | Vector
    ) -> Vector | int | float:
        if isinstance(other, (int, float)):
            new_x = round(self.x * other, 2)
            new_y = round(self.y * other, 2)
            return Vector(new_x, new_y)
        elif isinstance(other, Vector):
            x_dot = self.x * other.x
            y_dot = self.y * other.y
            return x_dot + y_dot

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        vector_x = end_point[0] - start_point[0]
        vector_y = end_point[1] - start_point[1]
        return Vector(vector_x, vector_y)

    def get_length(self) -> int | float:
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def get_normalized(self) -> Vector:
        normalized_x = self.x / Vector.get_length(self)
        normalized_y = self.y / Vector.get_length(self)
        return Vector(normalized_x, normalized_y)

    def angle_between(self, vector2: Vector) -> int:
        dot_product = self.__mul__(vector2)
        len_first = self.get_length()
        len_second = vector2.get_length()
        cos_a = dot_product / (len_first * len_second)
        angle_radians = math.acos(cos_a)
        angle_degrees = math.degrees(angle_radians)
        return round(angle_degrees)

    def get_angle(self) -> int:
        y_axis = Vector(0, 100)
        return self.angle_between(y_axis)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
        new_x = self.x * cos_theta - self.y * sin_theta
        new_y = self.x * sin_theta + self.y * cos_theta
        return Vector(new_x, new_y)
