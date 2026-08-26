from __future__ import annotations
from math import acos, degrees, radians, cos, sin, ceil


class Vector:
    def __init__(self, x_coord: int | float, y_coord: int | float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, vector2: Vector) -> Vector:
        return Vector(self.x + vector2.x, self.y + vector2.y)

    def __sub__(self, vector2: Vector) -> Vector:
        return Vector(self.x - vector2.x, self.y - vector2.y)

    def __mul__(self, vector2: int | float | Vector) -> Vector | int | float:
        if isinstance(vector2, Vector):
            return (self.x * vector2.x) + (self.y * vector2.y)
        return Vector(self.x * vector2, self.y * vector2)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> int | float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, vector2: Vector) -> int:
        return ceil(degrees(acos((self * vector2)
                                 / (self.get_length()
                                    * vector2.get_length()))))

    def get_angle(self) -> int:
        magnitude = self.get_length()
        cos_a = self.y / magnitude
        angle_radians = acos(cos_a)
        angle_degrees = degrees(angle_radians)
        return round(angle_degrees)

    def rotate(self, degrees: int) -> Vector:
        radian = radians(degrees)
        cos_theta = cos(radian)
        sin_theta = sin(radian)
        new_x = self.x * cos_theta - self.y * sin_theta
        new_y = self.x * sin_theta + self.y * cos_theta
        return Vector(new_x, new_y)
