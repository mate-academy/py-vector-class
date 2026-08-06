import math
from typing import Tuple


class Vector:
    def __init__(self, x_type: float, y_type: float) -> None:
        self.x = round(x_type, 2)
        self.y = round(y_type, 2)

    def __add__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            new_x = self.x + other.x
            new_y = self.y + other.y
            return Vector(new_x, new_y)
        else:
            raise TypeError("Unsupported operand type. "
                            "You can only add two "
                            "Vector objects together.")

    def __sub__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            new_x = self.x - other.x
            new_y = self.y - other.y
            return Vector(new_x, new_y)
        else:
            raise TypeError("Unsupported operand type. "
                            "You can only subtract "
                            "a Vector object from another "
                            "Vector object.")

    def __mul__(self, other: "Vector") -> float:
        if isinstance(other, Vector):
            dot_product = self.x * other.x + self.y * other.y
            return dot_product
        elif isinstance(other, (int, float)):
            new_x = self.x * other
            new_y = self.y * other
            return Vector(new_x, new_y)
        else:
            raise TypeError("Unsupported operand type. "
                            "You can only multiply "
                            "a Vector by another "
                            "Vector or a scalar.")

    @classmethod
    def create_vector_by_two_points(cls, start_point: Tuple[float, float],
                                    end_point: Tuple[float, float]) \
            -> "Vector":
        start_x, start_y = start_point
        end_x, end_y = end_point
        new_x = round(end_x - start_x, 2)
        new_y = round(end_y - start_y, 2)
        return cls(new_x, new_y)

    def get_length(self) -> float:
        length = math.sqrt(self.x ** 2 + self.y ** 2)
        return round(length, 15)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length != 0:
            new_x = self.x / length
            new_y = self.y / length
            return Vector(new_x, new_y)
        else:
            return Vector(0, 0)

    def angle_between(self, other: "Vector") -> float:
        if isinstance(other, Vector):
            cos_angle = (self.x * other.x + self.y * other.y) \
                / (self.get_length() * other.get_length())
            angle_in_radians = math.acos(cos_angle)
            angle_in_degrees = math.degrees(angle_in_radians)
            return round(angle_in_degrees, 0)
        else:
            raise TypeError("Unsupported operand type. "
                            "You can only calculate "
                            "the angle between two "
                            "Vector objects.")

    def get_angle(self) -> float:
        cos_angle = self.y / self.get_length()
        angle_in_radians = math.acos(cos_angle)
        angle_in_degrees = math.degrees(angle_in_radians)
        return round(angle_in_degrees, 0)

    def rotate(self, degrees: int) -> "Vector":
        angle_in_radians = math.radians(degrees)
        cos_theta = math.cos(angle_in_radians)
        sin_theta = math.sin(angle_in_radians)
        new_x = self.x * cos_theta - self.y * sin_theta
        new_y = self.x * sin_theta + self.y * cos_theta
        return Vector(new_x, new_y)
