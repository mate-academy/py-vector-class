from __future__ import annotations
import math


class Vector:
    def __init__(self, _x: float, _y: float) -> None:
        self.x = round(_x, 2)
        self.y = round(_y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector) -> float:
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            raise ValueError()
        return Vector(round(self.x / length, 2), round(self.y / length, 2))

    def angle_between(self, other: Vector) -> int:
        dot_product = self.x * other.x + self.y * other.y
        len_product = self.get_length() * other.get_length()
        if len_product == 0:
            raise ValueError()
        cos_a = dot_product / len_product
        cos_a = max(min(cos_a, 1), -1)
        angle_deg = math.degrees(math.acos(cos_a))
        return round(angle_deg)

    def get_angle(self) -> int:
        y_axis = Vector(0, 1)
        return self.angle_between(y_axis)

    def rotate(self, degrees: int) -> Vector:
        radians = math.radians(degrees)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
        x_new = self.x * cos_theta - self.y * sin_theta
        y_new = self.x * sin_theta + self.y * cos_theta
        return Vector(round(x_new, 2), round(y_new, 2))
