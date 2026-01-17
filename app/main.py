from __future__ import annotations
import math


class Vector:
    def __init__(self, x: float | int, y: float | int):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other)-> Vector:
        return Vector(x=self.x + other.x,
                      y=self.y + other.y)

    def __sub__(self, other)-> Vector:
        return Vector(x=self.x - other.x,
                      y=self.y - other.y)

    def __mul__(self, other: Vector | int | float)-> Vector | int | float:
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector(x=other * self.x,
                      y=other * self.y)

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple)-> Vector:
        return cls(x=list(end_point)[0] - list(start_point)[0],
                   y=list(end_point)[1] - list(start_point)[1])

    def get_length(self)-> float | int:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        initial_length = self.get_length()
        normalized_x = self.x / initial_length
        normalized_y = self.y / initial_length
        return Vector(x=normalized_x,
                      y=normalized_y)

    def angle_between(self, other: Vector)-> int:
        dot_product = self.__mul__(other)
        product_of_magnitudes = (self.get_length()
                                 * other.get_length())
        value_of_arccosine = math.acos(dot_product /
                                       product_of_magnitudes)
        angle = round(math.degrees(value_of_arccosine))
        return angle

    def get_angle(self)-> int:
        radian_angle_to_y_axis = math.atan2(self.x, self.y)
        degrees_angle_to_y_axis = abs(math.degrees(radian_angle_to_y_axis))
        return round(degrees_angle_to_y_axis)

    def rotate(self, degrees: int)-> Vector:
        degrees_to_radians = math.radians(degrees)
        sinus_value = math.sin(degrees_to_radians)
        cosine_value = math.cos(degrees_to_radians)
        new_x = cosine_value * self.x - sinus_value * self.y
        new_y = sinus_value * self.x + cosine_value * self.y
        return Vector(x=new_x, y=new_y)

    pass
