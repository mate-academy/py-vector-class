from typing import Union
import math


class Vector:
    def __init__(self, x_point: int | float, y_point: int | float) -> None:
        self.x = round(x_point, 2)
        self.y = round(y_point, 2)

    def __add__(self, other: Union["Vector", int | float]) -> "Vector":
        x_point = round(self.x + other.x, 2)
        y_point = round(self.y + other.y, 2)
        return Vector(x_point, y_point)

    def __sub__(self, other: Union["Vector", int | float]) -> "Vector":
        x_point = round(self.x - other.x, 2)
        y_point = round(self.y - other.y, 2)
        return Vector(x_point, y_point)

    def __mul__(self, other: Union["Vector", int, float])\
            -> Union["Vector", float]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        return Vector(round(self.x * other, 2),
                      round(self.y * other, 2))

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> "Vector":
        x_point = round(end_point[0] - start_point[0], 2)
        y_point = round(end_point[1] - start_point[1], 2)
        return cls(x_point, y_point)

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> "Vector":
        return Vector(round(self.x / self.get_length(), 2),
                      round(self.y / self.get_length(), 2))

    def angle_between(self, other: Union["Vector", int, float]) -> int | float:
        dot_product = self.x * other.x + self.y * other.y
        magnitude_product = self.get_length() * other.get_length()
        angle_rad = math.acos(dot_product / magnitude_product)
        angle_deg = math.degrees(angle_rad)
        return int(round(angle_deg))

    def get_angle(self) -> int:
        cos_a = self.y / self.get_length()
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, other: Union["Vector", int, float]) -> "Vector":
        angle_rad = math.radians(other)
        cos_theta = math.cos(angle_rad)
        sin_theta = math.sin(angle_rad)
        rot_x = self.x * cos_theta - self.y * sin_theta
        rot_y = self.x * sin_theta + self.y * cos_theta
        return Vector(round(rot_x, 2), round(rot_y, 2))
